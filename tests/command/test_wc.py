from cli.command.wc import Wc


oneline_src = 'tests/resources/oneline.txt'
multiline_src = 'tests/resources/multiline.txt'

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
    wc = Wc(['tests/resources/trash.txt'])
    assert wc.execute() == 'wc: tests/resources/trash.txt: no such file or directory\n'


def test_dir():
    wc = Wc(['tests/resources'])
    assert wc.execute() == 'wc: tests/resources: is a directory\n'


def test_with_data():
    wc = Wc([])
    data = 'hello world!\n\n!dlrow olleh\n'
    assert wc.execute(data) == '4\t4\t27\n'


def test_with_data_and_args():
    wc = Wc([oneline_src, multiline_src])
    data = 'hello world!\n\n!dlrow olleh\n'
    assert wc.execute(data) == f'1\t2\t14\t{oneline_src}\n8\t6\t40\t{multiline_src}\n'
