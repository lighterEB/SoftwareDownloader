import pathlib

import qt5_applications._applications


from ._version import get_versions
__version__ = get_versions()['version']
del get_versions


_root = pathlib.Path(__file__).absolute().parent
_bin = _root.joinpath('Qt', 'bin')
_plugins = _root.joinpath('Qt', 'plugins')


def _application_names():
    return [*qt5_applications._applications.application_paths.keys()]


def _application_path(name):
    return _bin.joinpath(qt5_applications._applications.application_paths[name])
