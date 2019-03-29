import os

from cli.command.ls import Ls

directory = os.path.join('tests', 'resources', 'directory')
file = os.path.join('tests', 'resources', 'directory', 'file.txt')


def test_ls_dir():
    ls = Ls([directory]).execute()
    assert ls == '\n'.join(os.listdir(os.path.join(os.getcwd(), directory))) + '\n'


def test_ls_file():
    ls = Ls([file]).execute()
    assert ls == os.path.realpath(file) + '\n'


def test_ls_more_than_one_arg():
    ls = Ls(['arg1', 'arg2']).execute()
    assert ls == 'ls: 0 or 1 argument expected\n'


def test_ls_current():
    ls = Ls([]).execute()
    assert ls == '\n'.join(os.listdir(os.getcwd())) + '\n'
