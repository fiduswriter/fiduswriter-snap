#!/usr/bin/env python3
import os
from subprocess import call

SNAP = os.environ.get('SNAP')
SNAP_DATA = os.environ.get('SNAP_DATA')
CONFIGURE_PATH = '{}/configuration.py'.format(SNAP_DATA)

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
