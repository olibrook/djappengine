#!/usr/bin/env python
import os
import sys
import code
import contextlib
import argparse

import dev_appserver
import wrapper_util


def main():
    parser = argparse.ArgumentParser(
        description="Start an interactive shell in an App Engine environment."
    )
    parser.add_argument('yaml_path')
    args = parser.parse_args()
    with appengine_environ(args.yaml_path):
        code.interact()


@contextlib.contextmanager
def appengine_environ(yaml_path):
    """Set up and tear down an environment as though running an application
    through `dev_appserver.py`.

    Usage:

        with appengine_environ(yaml_path):
            # Play with the datastore
            pass

    """

    # Initialize as though we are running `dev_appserver.py`.

    wrapper_util.reject_old_python_versions((2, 7))

    _DIR_PATH = wrapper_util.get_dir_path(dev_appserver.__file__, os.path.join('lib', 'ipaddr'))
    _PATHS = wrapper_util.Paths(_DIR_PATH)
    script_name = 'dev_appserver.py'
    sys.path = (_PATHS.script_paths(script_name) + _PATHS.scrub_path(script_name, sys.path))

    # Initialize as though `dev_appserver.py` is about to run our app, using all the
    # configuration provided in app.yaml.

    import google.appengine.tools.devappserver2.application_configuration as application_configuration
    import google.appengine.tools.devappserver2.devappserver2 as devappserver2
    import google.appengine.tools.devappserver2.python.sandbox as sandbox
    import google.appengine.tools.devappserver2.wsgi_request_info as wsgi_request_info

    # The argparser is the easiest way to get the default options.
    options = devappserver2.PARSER.parse_args([yaml_path])
    configuration = application_configuration.ApplicationConfiguration(options.config_paths)

    storage_path = devappserver2._get_storage_path(options.storage_path, configuration.app_id)
    dispatcher = None
    request_data = wsgi_request_info.WSGIRequestInfo(dispatcher)

    devappserver2._setup_environ(configuration.app_id)
    apis = devappserver2.DevelopmentServer._create_api_server(request_data, storage_path, options, configuration)

    # Enable App Engine libraries without enabling the full sandbox.
    module = configuration.modules[0]
    for l in sandbox._enable_libraries(module.normalized_libraries):
        sys.path.insert(0, l)

    apis.start()
    try:
        yield
    finally:
        apis.quit()


if __name__ == '__main__':
    main()
