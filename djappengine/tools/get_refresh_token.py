#!/usr/bin/env python
import argparse
import sys

from oauth2client import tools
from oauth2client.client import OAuth2WebServerFlow
from oauth2client.file import Storage


def main():
    """Gets an oauth2 refresh token and saves the result to a file.

    Many apps need to work with Google APIs in background tasks and use
    `oauth2client.appengine.AppAssertionCredentials` to allow an app to own its
    own documents, calendars, etc. This does not work on `dev_appserver`.

    As a workaround during development, create a refresh token for the current
    *developer* and let the app use this token instead. Each developer
    should then set up his/her own resources on Google's APIs which the
    development app can access without interfering with other developers.

    This should be a one-time setup step for development and is independent
    of any user-management/auth system in use.

    Usage example with the Calendar API, after generating a token:

        import httplib2

        from google.appengine.api import memcache
        from apiclient import discovery
        from oauth2client.appengine import AppAssertionCredentials
        from oauth2client import client

        DEBUG = True
        PATH_TO_CREDENTIALS = 'appengine/credentials.json'

        def _get_credentials():
            if DEBUG:
                with open(PATH_TO_CREDENTIALS, 'r') as f:
                    s = f.read()
                return client.Credentials.new_from_json(s)
            else:
                return AppAssertionCredentials()

        service = discovery.build(
            serviceName='calendar',
            version='v3',
            developerKey=settings.GOOGLE_API_KEY,
            http=_get_credentials().authorize(httplib2.Http(memcache))
        )

        calendar = service.calendars().get(calendarId='123').execute()


    """
    argparser = argparse.ArgumentParser(
        description="Gets an oauth2 refresh token for a user and saves the result to a file.",
        parents=[tools.argparser],
    )
    argparser.add_argument('--client_id')
    argparser.add_argument('--client_secret')
    argparser.add_argument('--scopes')
    argparser.add_argument('--output', default='appengine/credentials.json')

    flags = argparser.parse_args(sys.argv[1:])

    flow = OAuth2WebServerFlow(
        client_id=flags.client_id,
        client_secret=flags.client_secret,
        scope=flags.scopes,
        user_agent='get-refresh-token/1.0',
        approval_prompt='force'
    )

    storage = Storage(flags.output)
    credentials = storage.get()
    if credentials is None or credentials.invalid:
        tools.run_flow(flow, storage, flags)
    print("Credentials saved to '%s'" % flags.output)


if __name__ == '__main__':
    main()
