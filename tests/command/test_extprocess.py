from cli.command.extprocess import ExternalProcess, CommandNotFoundError
import pytest


def test_script():
    process = ExternalProcess('bash', ['tests/resources/script.sh'])
    assert process.execute() == 'hello   world!\nand once more\n'


def test_unknown_program():
    process = ExternalProcess('abacaba  228', [])
    with pytest.raises(CommandNotFoundError):
        process.execute()


def test_external_cat_with_data():
    process = ExternalProcess('cat', [])
    assert process.execute('some output from previous command') == 'some output from previous command'


def test_external_cat_with_data_and_args():
    process = ExternalProcess('cat', ['tests/resources/oneline.txt'])
    assert process.execute('some output from previous command') == 'hello  world \n'