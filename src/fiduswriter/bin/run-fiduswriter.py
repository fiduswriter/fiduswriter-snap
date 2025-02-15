#!/usr/bin/env python3
import os
import sys
import multiprocessing
import ast
import socket
from subprocess import check_output, CalledProcessError, Popen
from time import sleep

SNAP = os.environ.get("SNAP")
SNAP_DATA = os.environ.get("SNAP_DATA")
CONFIGURE_PATH = f"{SNAP_DATA}/configuration.py"
PASSWORD_PATH = f"{SNAP_DATA}/mysql/fiduswriter_password"

def port_check(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    try:
        s.connect(('127.0.0.1', port))
        return False
    except OSError:
        return True


def get_valid_ports(config):
    """Parse WS_URLS configuration with validation"""
    ports = []
    default_port = getattr(config, 'PORT', 4386)

    urls = getattr(config, 'WS_URLS', [])
    if not urls:
        # Default to number of cores
        cores = multiprocessing.cpu_count()
        port = default_port
        while len(ports) < cores:
            if port_check(port):
                ports.append(port)
            port += 1
        configuration_line = f"\nWS_URLS = {ports}"
        with open(CONFIGURE_PATH, "a") as config_file:
            config_file.write(configuration_line)
        return ports

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
                    f"{SNAP}/bin/fiduswriter",
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
                f"{SNAP}/bin/wait_for_mysql.sh",
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

    sys.path.append(SNAP_DATA)

    try:
        check_output(
            [
                f"{SNAP}/bin/fiduswriter",
                "transpile",
                "--pythonpath", SNAP_DATA
            ]
        )
    except CalledProcessError:
        sys.exit(1)

    import configuration
    ports = get_valid_ports(configuration)

    processes = []
    for port in ports:
        proc = Popen([
            f"{SNAP}/bin/fiduswriter",
            "runserver",
            f"{port}",
            "--pythonpath", SNAP_DATA
        ])
        processes.append(proc)

    # Wait for all processes
    for proc in processes:
        proc.wait()
