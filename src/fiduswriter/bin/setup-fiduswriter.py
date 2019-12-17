#!/usr/bin/env python3
import os
import sys
from subprocess import call
from time import sleep

SNAP = os.environ.get('SNAP')
SNAP_DATA = os.environ.get('SNAP_DATA')
CONFIGURE_PATH = '{}/configuration.py'.format(SNAP_DATA)
PASSWORD_PATH = '{}/mysql/fiduswriter_password'.format(SNAP_DATA)

if __name__ == '__main__':
    if os.getuid() != 0:
        print('This script must be run by root')
        sys.exit(1)
    if not os.path.isfile(CONFIGURE_PATH):
        print('Configuration file missing')
        sys.exit(1)  # The configuration hook is not done yet.
    timer = 0

    # We wait for the password file to be created
    while timer < 10 and not os.path.isfile(PASSWORD_PATH):
        timer += 1
        sleep(1)

    call([
        '{}/bin/fiduswriter'.format(SNAP),
        'setup',
        '--no-force-transpile',
        '--pythonpath',
        SNAP_DATA
    ])
