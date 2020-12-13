import os
import pathlib
import sys
import sysconfig

import PyQt5
import qt5_tools

from ._version import get_versions
__version__ = get_versions()['version']
del get_versions

import pyqt5_plugins.utilities


root = pathlib.Path(__file__).resolve().parent
# TODO: so apparently qml wants it all lower case...
if sys.platform == 'win32':
    root = pathlib.Path(pyqt5_plugins.utilities.fspath(root).lower())
plugins = root.joinpath('Qt', 'plugins')

pyqt5_root = pathlib.Path(PyQt5.__file__).resolve().parent
pyqt5_qml_path = pyqt5_root.joinpath('Qt', 'qml')
pyqt5_plugins_path = pyqt5_root.joinpath('Qt', 'plugins')


def create_environment(reference=None):
    if reference is None:
        reference = dict(os.environ)
    environment = qt5_tools.create_environment(reference=reference)

    if sys.platform == 'linux':
        environment.update(pyqt5_plugins.utilities.add_to_env_var_path_list(
            env=environment,
            name='LD_LIBRARY_PATH',
            before=[],
            after=[sysconfig.get_config_var('LIBDIR')],
        ))

    environment.update(pyqt5_plugins.utilities.add_to_env_var_path_list(
        env=environment,
        name='QT_PLUGIN_PATH',
        before=[],
        after=[
            pyqt5_plugins.utilities.fspath(pyqt5_plugins_path),
            pyqt5_plugins.utilities.fspath(plugins),
        ],
    ))
    # TODO: maybe also
    # PyQt5.QtCore.QLibraryInfo.location(
    #    PyQt5.QtCore.QLibraryInfo.PluginsPath,
    # )

    environment.update(pyqt5_plugins.utilities.add_to_env_var_path_list(
        env=environment,
        name='PYTHONPATH',
        before=sys.path,
        after=[''],
    ))
    environment.update(pyqt5_plugins.utilities.add_to_env_var_path_list(
        env=environment,
        name='PATH',
        before=sys.path,
        after=[''],
    ))

    return environment
