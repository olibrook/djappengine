#!/usr/bin/env python -i

""" A shell to play around with the local data, assuming:
dev_appserver.py . --use_sqlite --datastore_path=tmp/data """

import os
import logging

from environ import setup_environ

datastore_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "tmp", "data")
setup_environ(datastore_path=datastore_path)

app_id = os.environ['APPLICATION_ID']
