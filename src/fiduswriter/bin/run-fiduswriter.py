#!/usr/bin/env python3
import os
import sys
import multiprocessing
import ast
from subprocess import check_output, CalledProcessError
from time import sleep

SNAP = os.environ.get("SNAP")
SNAP_DATA = os.environ.get("SNAP_DATA")
CONFIGURE_PATH = "{}/configuration.py".format(SNAP_DATA)
PASSWORD_PATH = "{}/mysql/fiduswriter_password".format(SNAP_DATA)

def get_valid_ports(config):
    """Parse WS_URLS configuration with validation"""
    ports = []
    default_port = getattr(config, 'PORT', 4386)

    urls = getattr(config, 'WS_URLS', [])
    if not urls:
        # Default to number of cores
        cores = multiprocessing.cpu_count()
        return list(range(default_port, default_port + cores))

    for entry in urls:
        try:
            # Handle both int and string representations
            if isinstance(entry, int):
                port = entry
            elif isinstance(entry, str) and entry.isdigit():
                port = int(entry)
            elif entry is False:
                port = default_port
            else:
                continue

            if 1024 < port < 65535:
                ports.append(port)
        except (ValueError, TypeError):
            continue

    return ports or [default_port]


if __name__ == "__main__":
    if os.getuid() != 0:
        print("This script must be run by root")
        sys.exit(1)
    if not os.path.isfile(CONFIGURE_PATH):
        try:
            check_output(
                [
                    "{}/bin/fiduswriter".format(SNAP),
                    "startproject",
                    "--pythonpath",
                    SNAP_DATA,
                ]
            )
        except CalledProcessError:
            sys.exit(1)
    # We wait for the mysql server to start
    try:
        check_output(
            [
                "{}/bin/wait_for_mysql.sh".format(SNAP),
            ]
        )
    except CalledProcessError:
        sys.exit(1)
    # We wait for the password file to be created
    timer = 0
    while timer < 15 and not os.path.isfile(PASSWORD_PATH):
        timer += 0.1
        sleep(0.1)
    if not os.path.isfile(PASSWORD_PATH):
        print("Password file missing")
        # Something went wrong. This should have been caught by setup.
        sys.exit(1)

    try:
        sys.path.append(SNAP_DATA)
        import configuration
        ports = get_valid_ports(configuration)

        processes = []
        for port in ports:
            proc = subprocess.Popen([
                f"{SNAP}/bin/fiduswriter",
                "runserver",
                f"--port={port}",
                "--pythonpath", SNAP_DATA
            ])
            processes.append(proc)

        # Wait for all processes
        for proc in processes:
            proc.wait()

    except Exception as e:
            print(f"Error starting services: {str(e)}")
            sys.exit(1)
