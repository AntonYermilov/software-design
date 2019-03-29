from tests import init_standard_cli
import sys
from io import StringIO
from pathlib import Path


resources_src = Path('tests', 'resources')
oneline_src = str(resources_src / 'oneline.txt')
multiline_src = str(resources_src / 'multiline.txt')
resources_src = str(resources_src)


def test_execute_no_input():
    cli = init_standard_cli()
    assert cli.execute('    \n') == ''


def test_execute_simple_command():
    cli = init_standard_cli()
    assert cli.execute('echo arg1 arg2') == 'arg1 arg2\n'


def test_execute_pipe():
    cli = init_standard_cli()
    assert cli.execute('echo  "arg1   arg2"  arg3 | cat |  wc') == '1\t3\t17\n'


def test_execute_unexpected_pipe_error():
    cli = init_standard_cli()
    assert cli.execute(f'wc {oneline_src} | ') == 'cli: syntax error near unexpected token `|\'\n'


def test_execute_unexpected_backslash_error():
    cli = init_standard_cli()
    assert cli.execute(f'wc {oneline_src} \\') == 'cli: syntax error near unexpected token `\\\'\n'


def test_execute_matching_quote_error():
    cli = init_standard_cli()
    assert cli.execute(f'wc "{oneline_src}\'') == 'cli: no matching quote found\n'


def test_execute_set_variable():
    cli = init_standard_cli()
    assert cli.execute('a="hello world"') == ''


def test_get_variable():
    cli = init_standard_cli()
    cli.execute('a="hello world"')
    assert cli.execute('echo $a') == 'hello world\n'


def test_no_command_found_error():
    cli = init_standard_cli()
    sys.stderr = StringIO()
    assert cli.execute('echi "hello world"') == ''
    assert sys.stderr.getvalue() ==  'echi: command not found\n'


def test_cd_integration():
    cli = init_standard_cli()
    assert cli.execute('cd kwakwa') == 'cd: kwakwa: not a directory\n'


def test_ls_integration():
    cli = init_standard_cli()
    assert cli.execute('ls kwakwa') == 'ls: kwakwa: no such file or directory\n'
