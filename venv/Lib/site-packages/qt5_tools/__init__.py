import os

import qt5_applications


from ._version import get_versions
__version__ = get_versions()['version']
del get_versions


def bin_path():
    return qt5_applications._bin


def application_names():
    return qt5_applications._application_names()


def application_path(name):
    return qt5_applications._application_path(name)


def create_environment(reference=None):
    # noop for now, but just in case something needs added
    if reference is None:
        reference = os.environ

    return dict(reference)