from cli.env import Environment
from cli.command.extprocess import ExternalProcess
from cli.command.echo import Echo
from cli.command.cat import Cat
from cli.command.pwd import Pwd
from cli.command.wc import Wc
from cli.command.grep import Grep
from cli.command.exit import Exit
from tests import init_standard_env


def test_extprocess():
    env = init_standard_env()
    assert isinstance(env.get_command('bash', ['arg1', 'arg2']), ExternalProcess)


def test_echo():
    env = init_standard_env()
    assert isinstance(env.get_command('echo', ['arg1', 'arg2']), Echo)


def test_cat():
    env = init_standard_env()
    assert isinstance(env.get_command('cat', ['arg1', 'arg2']), Cat)


def test_pwd():
    env = init_standard_env()
    assert isinstance(env.get_command('pwd', ['arg1', 'arg2']), Pwd)


def test_wc():
    env = init_standard_env()
    assert isinstance(env.get_command('wc', ['arg1', 'arg2']), Wc)


def test_grep():
    env = init_standard_env()
    assert isinstance(env.get_command('grep', ['arg1', 'arg2']), Grep)


def test_exit():
    env = init_standard_env()
    assert isinstance(env.get_command('exit', ['arg1', 'arg2']), Exit)


def test_set_variable():
    cur = Environment(commands={}, variables={})
    cur.set_variable('var1', 'val1')
    cur.set_variable('var2', 'val2')
    assert 'var1' in cur._variables and cur._variables['var1'] == 'val1'
    assert 'var2' in cur._variables and cur._variables['var2'] == 'val2'
    assert 'var3' not in cur._variables


def test_get_variable():
    cur = Environment(commands={}, variables={'var1': 'val1', 'var2': 'val2'})
    assert cur.get_variable('var1') == 'val1'
    assert cur.get_variable('var2') == 'val2'
    assert cur.get_variable('var3') == ''
