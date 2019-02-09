from tests import init_standard_cli


def test_execute_no_input():
    cli = init_standard_cli()
    assert cli.execute('    \n') == ''


def test_execute_simple_command():
    cli = init_standard_cli()
    assert cli.execute('echo arg1 arg2') == 'arg1 arg2\n'


def test_execute_pipe():
    cli = init_standard_cli()
    assert cli.execute('echo  "arg1   arg2"  arg3 | cat |  wc') == '2\t3\t17\n'


def test_execute_unexpected_pipe_error():
    cli = init_standard_cli()
    assert cli.execute('wc tests/resources/oneline.txt | ') == 'cli: syntax error near unexpected token `|\'\n'


def test_execute_unexpected_backslash_error():
    cli = init_standard_cli()
    assert cli.execute('wc tests/resources/oneline.txt \\') == 'cli: syntax error near unexpected token `\\\'\n'


def test_execute_matching_quote_error():
    cli = init_standard_cli()
    assert cli.execute('wc "tests/something\'') == 'cli: no matching quote found\n'


def test_execute_set_variable():
    cli = init_standard_cli()
    assert cli.execute('a="hello world"') == ''


def test_get_variable():
    cli = init_standard_cli()
    cli.execute('a="hello world"')
    assert cli.execute('echo $a') == 'hello world\n'


def test_no_command_found_error():
    cli = init_standard_cli()
    assert cli.execute('echi "hello world"') == 'echi: command not found\n'
