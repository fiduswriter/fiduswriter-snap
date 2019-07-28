#!/usr/bin/env python3
import os
from subprocess import call

SNAP_NAME = os.environ.get('SNAP_NAME')
SNAP = os.environ.get('SNAP')
SNAP_DATA = os.environ.get('SNAP_DATA')
CONFIGURE_PATH = '/var/snap/{}/current/configuration.py'.format(SNAP_NAME)

if __name__ == '__main__':
    if not os.path.isfile(CONFIGURE_PATH):
        call([
            '{}/bin/fiduswriter'.format(SNAP),
            'startproject',
            '--pythonpath',
            SNAP_DATA
        ])
    call([
        '{}/bin/fiduswriter'.format(SNAP),
        'runserver',
        '--pythonpath',
        SNAP_DATA
    ])
