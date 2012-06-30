#!/usr/bin/env python

import os, sys


# User dev_appserver.py for now
if 'runserver' in sys.argv:
    sys.stderr.write(
        "Error: please uses `dev_appserver.py` to run your development server\n")
    sys.exit(1)


# Set up the python path using dev_appserver
for path in os.environ.get('PATH').split(os.pathsep):
    if 'dev_appserver.py' in os.listdir(path):
        sdk_path = os.path.dirname(
            os.readlink(os.path.join(path, 'dev_appserver.py')))
        sys.path.insert(0, sdk_path)
        from dev_appserver import fix_sys_path
        fix_sys_path()
        # django 1.3 at top of path to obscure hobbled version
        sys.path.insert(0, os.path.join(sdk_path, 'lib', 'django_1_3'))

from django.core.management import execute_manager

try:
    import settings # Assumed to be in the same directory.
except ImportError:
    sys.stderr.write(
        "Error: Can't find the file `settings.py` in the directory"
        "containing %r. It appears you've customized things.\nYou'll have"
        "to run django-admin.py, passing it your settings module.\n(If the"
        "file `settings.py` does indeed exist, it's causing an ImportError"
        "somehow.)\n" % __file__)
    sys.exit(1)

if __name__ == "__main__": execute_manager(settings)
