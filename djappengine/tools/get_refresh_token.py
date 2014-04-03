import argparse
import sys

from oauth2client import tools
from oauth2client.client import OAuth2WebServerFlow
from oauth2client.file import Storage


def main():
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
