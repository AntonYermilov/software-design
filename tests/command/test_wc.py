from cli.command.wc import Wc
from pathlib import Path
import sys
from io import StringIO

resources_src = Path('tests', 'resources')
oneline_src = str(resources_src / 'oneline.txt')
multiline_src = str(resources_src / 'multiline.txt')
trash_src = str(resources_src / 'trash.txt')
win_src = str(resources_src / 'gitignore.dms')
resources_src = str(resources_src)

oneline_text = open(oneline_src, 'r').read()
multiline_text = open(multiline_src, 'r').read()


def test_one_file_oneline():
    wc = Wc([oneline_src])
    assert wc.execute() == f'1\t2\t14\t{oneline_src}\n'


def test_one_file_multiline():
    wc = Wc([multiline_src])
    assert wc.execute() == f'8\t6\t40\t{multiline_src}\n'


def test_multiple_files():
    wc = Wc([oneline_src, multiline_src])
    assert wc.execute() == f'1\t2\t14\t{oneline_src}\n8\t6\t40\t{multiline_src}\n'


def test_same_files_1():
    wc = Wc([oneline_src, oneline_src, oneline_src])
    assert wc.execute() == f'1\t2\t14\t{oneline_src}\n1\t2\t14\t{oneline_src}\n1\t2\t14\t{oneline_src}\n'


def test_same_files_2():
    wc = Wc([multiline_src, multiline_src])
    assert wc.execute() == f'8\t6\t40\t{multiline_src}\n8\t6\t40\t{multiline_src}\n'


def test_no_files():
    wc = Wc([])
    assert wc.execute() == ''


def test_file_not_exists():
    wc = Wc([trash_src])
    sys.stderr = StringIO()
    assert wc.execute() == ''
    assert sys.stderr.getvalue() == f'wc: {trash_src}: no such file or directory\n'


def test_dir():
    wc = Wc([resources_src])
    sys.stderr = StringIO()
    assert wc.execute() == ''
    assert sys.stderr.getvalue() == f'wc: {resources_src}: is a directory\n'


def test_with_data():
    wc = Wc([])
    data = 'hello world!\n\n!dlrow olleh\n'
    assert wc.execute(data) == '3\t4\t27\n'


def test_with_data_and_args():
    wc = Wc([oneline_src, multiline_src])
    data = 'hello world!\n\n!dlrow olleh\n'
    assert wc.execute(data) == f'1\t2\t14\t{oneline_src}\n8\t6\t40\t{multiline_src}\n'


def test_windows_endlines():
    wc = Wc([win_src])
    assert wc.execute() == f'104\t158\t1307\t{win_src}\n'
