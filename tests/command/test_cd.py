import os

from cli import Pwd, CLI
from cli.command.cd import Cd

directory = 'tests/resources/directory'


def restore_env(fun):
    def restored(*args, **kwargs):
        CLI.environment.set_variable('PWD', os.getcwd())
        fun(*args, **kwargs)
        CLI.environment.set_variable('PWD', os.getcwd())

    return restored


@restore_env
def test_cd_dir():
    cd = Cd([directory]).execute()
    current_dir = Pwd([]).execute()
    assert current_dir == os.path.join(os.getcwd(), directory) + '\n'
    assert not cd


@restore_env
def test_cd_back():
    cd = Cd(['..']).execute()
    current_dir = Pwd([]).execute()
    assert current_dir == os.path.join(os.getcwd(), os.path.realpath('..')) + '\n'
    assert not cd


@restore_env
def test_cd_home():
    cd = Cd([]).execute()
    current_dir = Pwd([]).execute()
    assert current_dir == os.path.expanduser('~') + '\n'
    assert not cd


@restore_env
def test_cd_non_existing_path():
    previous_dir = Pwd([]).execute()
    cd = Cd(['кукарямба']).execute()
    current_dir = Pwd([]).execute()
    assert current_dir == previous_dir
    assert cd
