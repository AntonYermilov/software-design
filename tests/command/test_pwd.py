from cli.command.pwd import Pwd
import os


root_dir = f'{os.getcwd()}\n'


def test_pwd():
    pwd = Pwd([])
    assert pwd.execute() == root_dir


def test_pwd_with_args():
    pwd = Pwd(['hello', 'world'])
    assert pwd.execute() == root_dir


def test_pwd_with_data():
    pwd = Pwd(['hello', 'world'])
    assert pwd.execute('hello world') == root_dir
