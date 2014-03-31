"""Collect request handlers and wsgi apps which require initialization (eg. path adjustment)
inside the handlers package.

"""

import os
import logging

import django.core.signals as signals
from google.appengine.api.app_identity import get_application_id

# Environ and path adjustments.
ON_PRODUCTION_SERVER = 'google' in os.environ.get('SERVER_SOFTWARE', '').lower()


def get_settings_name():
    if ON_PRODUCTION_SERVER:
        return '{{ project_name }}.settings.live'
    else:
        return '{{ project_name }}.settings.dev'


def django_setup_teardown(f):

    # Database connections are opened on demand in Django, but need to be
    # closed explicitly. This is done by sending a `request_finished`
    # signal in Django's default WSGI handler.
    #
    # App Engine's built-in handlers don't normally trigger the signals - wrap
    # them with this decorator to prevent leaking open DB connections.
    #
    # http://code.google.com/p/googleappengine/issues/detail?id=10118

    def wrapper(*args, **kwargs):
        logging.info('Request started')
        signals.request_started.send(sender=f)
        try:
            return f(*args, **kwargs)
        finally:
            logging.info('Request finished')
            signals.request_finished.send(sender=f)

    return wrapper


# Override if not set explicitly
os.environ.setdefault("DJANGO_SETTINGS_MODULE", get_settings_name())
import fix_paths
