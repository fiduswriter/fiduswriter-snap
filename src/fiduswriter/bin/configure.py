#!/usr/bin/env python3
import os
import ast
import sys
import tempfile
from subprocess import call, check_output, CalledProcessError

SNAP = os.environ.get('SNAP')
SNAP_DATA = os.environ.get('SNAP_DATA')
CONFIGURE_PATH = '{}/configuration.py'.format(SNAP_DATA)


def is_python(string):
    try:
        ast.parse(string)
    except SyntaxError:
        return False
    return True


def is_configuration(f_path):
    filename = os.path.basename(f_path)[:-3]
    path = os.path.dirname(f_path)
    try:
        check_output([
            '{}/bin/fiduswriter'.format(SNAP),
            'help',
            '--pythonpath',
            path,
            '--settings',
            filename
        ])
    except CalledProcessError:
        return False
    return True


if __name__ == '__main__':
    if os.getuid() != 0:
        print('This script must be run by root')
        sys.exit()
    if not os.path.isfile(CONFIGURE_PATH):
        call([
            '{}/bin/fiduswriter'.format(SNAP),
            'startproject',
            '--pythonpath',
            SNAP_DATA
        ])
    with open(CONFIGURE_PATH, 'r') as file:
        configuration = file.read()
    f_path = tempfile.mktemp(
        prefix='configuration_',
        suffix='.py'
    )
    with open(f_path, 'w') as file:
        file.write(configuration)
    valid_configuration = False
    while valid_configuration is False:
        call([
            'nano',
            '--restricted',
            f_path
        ])
        with open(f_path, 'r') as file:
            new_configuration = file.read()
        if configuration == new_configuration:
            valid_configuration = True
        elif is_python(new_configuration) and is_configuration(f_path):
            valid_configuration = True
        else:
            print('The configuration file is no longer valid.')
            fix_it = input('Do you want to fix it? [Y/n] ')
            if fix_it.lower() not in ['', 'y', 'yes']:
                os.remove(f_path)
                sys.exit()
    os.remove(f_path)
    if configuration != new_configuration:
        with open(CONFIGURE_PATH, 'w') as file:
            file.write(new_configuration)
        print(
            'Your settings have been updated. '
            'Please wait while we set everything up.'
        )
        call([
            '{}/bin/fiduswriter'.format(SNAP),
            'setup',
            '--no-force-transpile',
            '--pythonpath',
            SNAP_DATA
        ])
        call(['snapctl', 'restart', 'fiduswriter.daemon'])
        print('Fidus Writer has been updated and restarted.')
