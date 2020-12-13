import os
import subprocess
import sys
import sysconfig

import pytest

import qt5_applications


fspath = getattr(os, 'fspath', str)


def add_to_env_var_path_list(environment, name, before, after):
    return {
        name: os.pathsep.join((
            *before,
            environment.get(name, ''),
            *after
        ))
    }


def create_environment(reference):
    environment = dict(reference)

    if sys.platform == 'linux':
        environment.update(add_to_env_var_path_list(
            environment=environment,
            name='LD_LIBRARY_PATH',
            before=[''],
            after=[sysconfig.get_config_var('LIBDIR')],
        ))
    if sys.platform == 'win32':
        environment.update(add_to_env_var_path_list(
            environment=environment,
            name='PATH',
            before=[''],
            after=[sysconfig.get_path('scripts')],
        ))

    return environment


def test_designer():
    with pytest.raises(subprocess.TimeoutExpired):
        subprocess.run(
            [
                fspath(qt5_applications._application_path('designer')),
            ],
            check=True,
            env={**create_environment(os.environ), 'QT_DEBUG_PLUGINS': '1'},
            timeout=10,
        )


def test_qmlscene():
    with pytest.raises(subprocess.TimeoutExpired):
        subprocess.run(
            [
                fspath(qt5_applications._application_path('qmlscene')),
            ],
            check=True,
            env={**create_environment(os.environ), 'QT_DEBUG_PLUGINS': '1'},
            timeout=10,
        )

# TODO: hangs on GHA
# def test_language():
#     completed_process = subprocess.run(
#         [
#             fspath(qt5_applications._application_path('qtdiag')),
#         ],
#         check=True,
#         env={**os.environ, 'LANGUAGE': 'de_DE'},
#         stdout=subprocess.PIPE,
#         timeout=30,
#     )
#
#     assert b'de_DE' in completed_process.stdout
