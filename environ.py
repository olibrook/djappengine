import logging
import os
import re
import sys


HOST_REGEX = re.compile('^(localhost|(?:\d+\.\d+\.\d+\.\d+))(?:\:(\d+))?')
ROOT_PATH = os.path.normpath(os.path.abspath(os.path.dirname(__file__)))


def add_lib_to_path():
    sys.path.insert(0, os.path.join(ROOT_PATH, "lib"))


def get_sdk_lib_path(sdk_path, name, version):
    return os.path.join(sdk_path, "lib", "-".join([name, version]))


def ensure_sdk_on_path():
    """Put the App Engine SDK on the PATH so that we can set up all the stubs
    and add the libraries from app.yaml to the PATH.
    """
    sdk_path, test_path = "", ""

    for path in os.environ["PATH"].split(os.pathsep):
        try:
            if "dev_appserver.py" in os.listdir(path):
                test_path = os.path.join(path, "dev_appserver.py")
                sdk_path = os.path.dirname(
                    os.readlink(test_path)
                    if os.path.islink(test_path)
                    else test_path
                )
                sys.path.insert(0, sdk_path)

                from dev_appserver import fix_sys_path
                fix_sys_path()

                # Presumably don't want to do this multiple times
                break
        except OSError:
            pass

    return sdk_path


def setup_appengine_env(**stub_kwargs):
    """Try to set up the environment as if we were running on dev_appserver.

    Calling this should make all App Engine service stubs available and load
    all libraries in app.yaml so that they're available too.
    """
    host, port = "127.0.0.1", "8000"

    # The SDK has to be on the PATH before doing any of the other dev_appserver
    # PATH munging stuff
    sdk_path = ensure_sdk_on_path()

    from google.appengine.api import appinfo
    from google.appengine.tools.dev_appserver import LoadAppConfig, SetupStubs
    from google.appengine.tools.dev_appserver_main import DEFAULT_ARGS

    # Certain stubs expect these SERVER_* env vars to be set
    matches = HOST_REGEX.match(sys.argv[-1])
    host, port = matches.groups() if matches else (host, port)

    os.environ.setdefault("SERVER_NAME", ":".join([host, port]))
    os.environ.setdefault("SERVER_PORT", port)

    options = DEFAULT_ARGS.copy()
    options.update({
        "use_sqlite": True,
        "high_replication": True,
    })
    options.update(stub_kwargs)

    conf, _, _ = LoadAppConfig(ROOT_PATH, {}, default_partition="dev")
    SetupStubs(conf.application, **options)

    if conf.libraries:
        extra_paths = []

        for library in conf.libraries:
            version = library.version
            if version == "latest":
                version = (
                    appinfo._NAME_TO_SUPPORTED_LIBRARY[library.name]
                    .non_deprecated_versions[-1]
                )

            path = get_sdk_lib_path(sdk_path, library.name, version)
            extra_paths.append(path)

        if extra_paths:
            sys.path = extra_paths + sys.path


def setup_environ(**stub_kwargs):
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "{{ project_name }}.settings")

    add_lib_to_path()
    setup_appengine_env(**stub_kwargs)
