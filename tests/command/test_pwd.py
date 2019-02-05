from cli.command.pwd import Pwd


root_dir = 'software-design\n'


def test_pwd():
    pwd = Pwd([])
    assert pwd.execute()[-len(root_dir):] == root_dir


def test_pwd_with_args():
    pwd = Pwd(['hello', 'world'])
    assert pwd.execute()[-len(root_dir):] == root_dir


def test_pwd_with_data():
    pwd = Pwd(['hello', 'world'])
    assert pwd.execute('hello world')[-len(root_dir):] == root_dir
