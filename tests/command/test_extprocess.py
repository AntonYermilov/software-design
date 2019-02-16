from cli.command.extprocess import ExternalProcess, CommandNotFoundError
import pytest
import os


def test_unknown_program():
    process = ExternalProcess('abacaba  228', [])
    with pytest.raises(CommandNotFoundError):
        process.execute()


def test_posix_script():
    if os.name == 'posix':
        process = ExternalProcess('bash', ['tests/resources/script.sh'])
        assert process.execute() == 'hello   world!\nand once more\n'


def test_posix_external_cat_with_data():
    if os.name == 'posix':
        process = ExternalProcess('cat', [])
        assert process.execute('some output from previous command') == 'some output from previous command'


def test_posix_external_cat_with_data_and_args():
    if os.name == 'posix':
        process = ExternalProcess('cat', ['tests/resources/oneline.txt'])
        assert process.execute('some output from previous command') == 'hello  world \n'