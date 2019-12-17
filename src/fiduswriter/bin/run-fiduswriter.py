#!/usr/bin/env python3
import os
import sys
from subprocess import call

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
        # Something went wrong. This should have been caught by setup.
        sys.exit(1)
    if not os.path.isfile(PASSWORD_PATH):
        print('Password file missing')
        # Something went wrong. This should have been caught by setup.
        sys.exit(1)

    call([
        '{}/bin/fiduswriter'.format(SNAP),
        'runserver',
        '--pythonpath',
        SNAP_DATA
    ])
