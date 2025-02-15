#!/usr/bin/env python3
import os
import sys
from subprocess import check_output, CalledProcessError
from time import sleep

SNAP = os.environ.get("SNAP")
SNAP_DATA = os.environ.get("SNAP_DATA")
CONFIGURE_PATH = f"{SNAP_DATA}/configuration.py"
PASSWORD_PATH = f"{SNAP_DATA}/mysql/fiduswriter_password"


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
            [f"{SNAP}/bin/fiduswriter", "runserver", "--pythonpath", SNAP_DATA]
        )
    except CalledProcessError:
        sys.exit(1)
