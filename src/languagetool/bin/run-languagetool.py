#!/usr/bin/env python3
import os
import sys
from subprocess import call

SNAP_NAME = os.environ.get('SNAP_NAME')
SNAP = os.environ.get('SNAP')
SNAP_DATA = os.environ.get('SNAP_DATA')
sys.path.append(SNAP_DATA)

if __name__ == '__main__':
    LT_PORT = False
    try:
        import configuration
        if hasattr(configuration, 'LT_PORT'):
            LT_PORT = configuration.LT_PORT
    except ModuleNotFoundError:
        LT_PORT = 4387
    if LT_PORT:
        call([
            'java',
            '-cp', '{}/lt/languagetool-server.jar'.format(SNAP), 'org.languagetool.server.HTTPServer',
            '--port', '{}'.format(LT_PORT)
        ])
