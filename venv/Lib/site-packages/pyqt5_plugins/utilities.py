import os

import pyqt5_plugins


fspath = getattr(os, 'fspath', str)


diagnostic_variables_to_print = [
    'DISPLAY',
    'LD_LIBRARY_PATH',
    'PYQTDESIGNERPATH',
    'PYTHONPATH',
    'PATH',
    'QML2_IMPORT_PATH',
    'QT_DEBUG_PLUGINS',
    'QT_PLUGIN_PATH',
]


def add_to_env_var_path_list(env, name, before, after):
    return {
        name: os.pathsep.join((
            *before,
            env.get(name, ''),
            *after
        ))
    }


def print_environment_variables(env, *variables):
    for name in variables:
        value = env.get(name)
        if value is None:
            print('{} is not set'.format(name))
        else:
            print('{}: {}'.format(name, value))


def mutate_qml_path(env, paths):
    env.update(add_to_env_var_path_list(
        env=env,
        name='QML2_IMPORT_PATH',
        before=[*paths, fspath(pyqt5_plugins.pyqt5_qml_path)],
        after=[''],
    ))
