from cli.command.cat import Cat

oneline_src = 'tests/resources/oneline.txt'
multiline_src = 'tests/resources/multiline.txt'

oneline_text = open(oneline_src, 'r').read()
multiline_text = open(multiline_src, 'r').read()


def test_one_file_oneline():
    cat = Cat([oneline_src])
    assert cat.execute() == oneline_text


def test_one_file_multiline():
    cat = Cat([oneline_src])
    assert cat.execute() == oneline_text


def test_multiple_files():
    cat = Cat([oneline_src, multiline_src])
    assert cat.execute() == oneline_text + multiline_text


def test_same_files_1():
    cat = Cat([oneline_src, oneline_src, oneline_src])
    assert cat.execute() == oneline_text + oneline_text + oneline_text


def test_same_files_2():
    cat = Cat([multiline_src, multiline_src])
    assert cat.execute() == multiline_text + multiline_text


def test_no_files():
    cat = Cat([])
    assert cat.execute() == ''


def test_file_not_exists():
    cat = Cat(['tests/resources/trash.txt'])
    assert cat.execute() == 'cat: tests/resources/trash.txt: no such file or directory\n'


def test_dir():
    cat = Cat(['tests/resources'])
    assert cat.execute() == 'cat: tests/resources: is a directory\n'


def test_with_data():
    cat = Cat([])
    data = 'hello world!\n\n!dlrow olleh\n'
    assert cat.execute(data) == data


def test_with_data_and_args():
    cat = Cat([oneline_src, multiline_src])
    data = 'hello world!\n\n!dlrow olleh\n'
    assert cat.execute(data) == oneline_text + multiline_text
