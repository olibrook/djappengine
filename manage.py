#!/usr/bin/env python
import logging
import os
import subprocess
import sys

from environ import setup_environ

setup_environ()

# Don't allow `runserver` or `shell`

if 'runserver' in sys.argv:
    logging.warn('You should serve your local instance with dev_appserver. See `serve.sh`')
    subprocess.call('./serve.sh')


if 'shell' in sys.argv:
    logging.warn('You should run the shell with ./shell.py, see for more info.')
    subprocess.call('./shell.py')

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djappengine.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
