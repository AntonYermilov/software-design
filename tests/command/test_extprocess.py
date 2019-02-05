from cli.command.extprocess import ExternalProcess


def test_script():
    process = ExternalProcess('bash', ['tests/resources/script.sh'])
    assert process.execute() == 'hello   world!\nand once more\n'


def test_unknown_program():
    process = ExternalProcess('abacaba  228', [])
    assert process.execute() == 'abacaba  228: command not found\n'
