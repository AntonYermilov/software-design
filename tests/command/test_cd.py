import os

from cli import Pwd, CLI
from cli.command.cd import Cd

directory = 'tests/resources/directory'
initial_path = os.getcwd()


def restore_env(fun):
    def restored(*args, **kwargs):
        os.chdir(initial_path)
        fun(*args, **kwargs)
        os.chdir(initial_path)
    return restored


@restore_env
def test_cd_dir():
    cd = Cd([directory]).execute()
    current_dir = Pwd([]).execute()
    assert current_dir == os.path.join(initial_path, directory) + '\n'
    assert not cd


@restore_env
def test_cd_back():
    realpath = os.path.realpath('..')
    cd = Cd(['..']).execute()
    current_dir = Pwd([]).execute()
    assert current_dir == os.path.join(initial_path, realpath) + '\n'
    assert not cd


@restore_env
def test_cd_home():
    cd = Cd([]).execute()
    current_dir = Pwd([]).execute()
    assert current_dir == os.path.expanduser('~') + '\n'
    assert not cd
