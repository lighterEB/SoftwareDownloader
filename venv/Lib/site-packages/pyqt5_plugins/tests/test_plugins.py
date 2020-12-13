import os
import pathlib
import subprocess
import time

import pytest
import qt5_tools

import pyqt5_plugins
import pyqt5_plugins.examples.exampleqmlitem
import pyqt5_plugins.tests.testbutton
import pyqt5_plugins.tests.testbuttonplugin
import pyqt5_plugins.utilities


fspath = getattr(os, 'fspath', str)


vars_to_print = [
    *pyqt5_plugins.utilities.diagnostic_variables_to_print,
    pyqt5_plugins.examples.exampleqmlitem.test_path_env_var,
    pyqt5_plugins.tests.testbutton.test_path_env_var,
]


@pytest.fixture(name='environment')
def environment_fixture():
    environment = pyqt5_plugins.create_environment(os.environ)
    pyqt5_plugins.utilities.mutate_qml_path(environment, paths=qml2_import_paths)
    environment['QT_DEBUG_PLUGINS'] = '1'

    return environment


def run_for_file(
        *args,
        file_path,
        file_exists_timeout=60,
        file_write_time_allowance=5,
        **kwargs
):
    process = subprocess.Popen(*args, **kwargs)

    deadline = time.monotonic() + file_exists_timeout

    while True:
        time.sleep(1)

        if process.poll() is not None:
            raise Exception('process ended')

        if file_path.exists():
            break

        if time.monotonic() > deadline:
            raise Exception(
                'file not written with {} seconds'.format(file_exists_timeout),
            )

    time.sleep(file_write_time_allowance)

    return file_path.read_bytes()


def test_designer_creates_test_widget(tmp_path, environment):
    file_path = tmp_path/'tigger'
    environment[pyqt5_plugins.tests.testbutton.test_path_env_var] = fspath(file_path)

    widget_plugin_path = pathlib.Path(
        pyqt5_plugins.tests.testbuttonplugin.__file__,
    ).parent

    environment.update(pyqt5_plugins.utilities.add_to_env_var_path_list(
        env=environment,
        name='PYQTDESIGNERPATH',
        before=[fspath(widget_plugin_path)],
        after=[''],
    ))

    pyqt5_plugins.utilities.print_environment_variables(environment, *vars_to_print)

    contents = run_for_file(
        [fspath(qt5_tools.application_path('designer'))],
        env=environment,
        file_path=file_path,
    )

    assert contents == pyqt5_plugins.tests.testbutton.test_file_contents


qml2_import_paths = (pyqt5_plugins.utilities.fspath(pyqt5_plugins.root),)


def test_qmlscene_paints_test_item(tmp_path, environment):
    file_path = tmp_path/'eeyore'
    environment[pyqt5_plugins.examples.exampleqmlitem.test_path_env_var] = fspath(file_path)

    qml_example_path = pyqt5_plugins.utilities.fspath(
        pathlib.Path(pyqt5_plugins.examples.__file__).parent / 'qmlapp.qml'
    )

    pyqt5_plugins.utilities.print_environment_variables(environment, *vars_to_print)

    contents = run_for_file(
        [
            fspath(qt5_tools.application_path('qmlscene')),
            fspath(qml_example_path),
        ],
        env=environment,
        file_path=file_path,
    )

    assert contents == pyqt5_plugins.examples.exampleqmlitem.test_file_contents


def test_qmltestrunner_paints_test_item(tmp_path, environment):
    file_path = tmp_path/'piglet'
    environment[pyqt5_plugins.examples.exampleqmlitem.test_path_env_var] = fspath(file_path)

    qml_test_path = pyqt5_plugins.utilities.fspath(
        pathlib.Path(pyqt5_plugins.examples.__file__).parent / 'qmltest.qml'
    )

    pyqt5_plugins.utilities.print_environment_variables(environment, *vars_to_print)

    subprocess.run(
        [
            fspath(qt5_tools.application_path('qmltestrunner')),
            '-input',
            qml_test_path,
        ],
        check=True,
        env=environment,
        timeout=60,
    )

    assert (
            file_path.read_bytes()
            == pyqt5_plugins.examples.exampleqmlitem.test_file_contents
    )
