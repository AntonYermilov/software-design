from cli.command.grep import Grep
import sys
from io import StringIO
from pathlib import Path

resources_src = Path('tests', 'resources')
grep_test_src = str(resources_src / 'grep_test.txt')
grep_test_1_src = str(resources_src / 'grep_test_1.txt')
grep_test_2_src = str(resources_src / 'grep_test_2.txt')
resources_src = str(resources_src)


def test_no_arguments():
    grep = Grep([])
    sys.stderr = StringIO()
    assert grep.execute() == ''
    assert sys.stderr.getvalue() == 'usage: grep [-i] [-w] [-A N] pattern [file [file ...]]\n' \
                                    'grep: the following arguments are required: pattern, file\n'


def test_invalid_arguments():
    grep = Grep(['-i', '-j', 'pattern', 'file'])
    sys.stderr = StringIO()
    assert grep.execute() == ''
    assert sys.stderr.getvalue() == 'usage: grep [-i] [-w] [-A N] pattern [file [file ...]]\n' \
                                    'grep: unrecognized arguments: -j\n'


def test_matching():
    grep = Grep(['aca'])
    assert grep.execute('abacaba') == 'abacaba\n'


def test_not_matching():
    grep = Grep(['aca'])
    assert grep.execute('abadaba') == ''


def test_multiple_line_matching():
    grep = Grep(['aca'])
    assert grep.execute('abacaba\nabadaba\ncaca\ncac\naca\n') == 'abacaba\ncaca\naca\n'


def test_case_sensetive():
    grep = Grep(['aca'])
    assert grep.execute('abaCaba') == ''


def test_case_insensitive():
    grep = Grep(['-i', 'aca'])
    assert grep.execute('abaCaba') == 'abaCaba\n'


def test_without_word_regex():
    grep = Grep(['aca'])
    assert grep.execute('abacaba\naca\ncac acac\nca aca ac') == \
           'abacaba\naca\ncac acac\nca aca ac\n'


def test_with_word_regex():
    grep = Grep(['-w', 'aca'])
    assert grep.execute('abacaba\naca\ncac acac\nca aca ac') == \
           'aca\nca aca ac\n'


def test_without_after_context():
    grep = Grep(['aca'])
    assert grep.execute('abacaba\nval1\nval2\nacab bac\nval3\nval4\nval5') == \
           'abacaba\nacab bac\n'


def test_with_after_context():
    grep = Grep(['-A', '1', 'aca'])
    assert grep.execute('abacaba\nval1\nval2\nacab bac\nval3\nval4\nval5') == \
           'abacaba\nval1\n--\nacab bac\nval3\n'


def test_with_after_context_many_lines():
    grep = Grep(['-A', '2', 'aca'])
    assert grep.execute('abacaba\nval1\nval2\nacab bac\nval3\nval4\nval5') == \
           'abacaba\nval1\nval2\nacab bac\nval3\nval4\n'


def test_invalid_argument_type():
    grep = Grep(['-A', 'a', 'aca'])
    sys.stderr = StringIO()
    assert grep.execute() == ''
    assert sys.stderr.getvalue() == 'usage: grep [-i] [-w] [-A N] pattern [file [file ...]]\n' \
                                    'grep: argument -A/--after_context: invalid int value: \'a\'\n'


def test_from_file_1():
    grep = Grep(['hello', grep_test_1_src])
    assert grep.execute() == 'hello world\n'


def test_from_file_2():
    grep = Grep(['hell', grep_test_1_src])
    assert grep.execute() == 'hello world\ngo to hell\n'


def test_from_file_3():
    grep = Grep(['-w', 'hell', grep_test_1_src])
    assert grep.execute() == 'go to hell\n'


def test_from_file_4():
    grep = Grep(['-i', 'hell', grep_test_1_src])
    assert grep.execute() == 'hello world\ngo to hell\nHellO!\n'


def test_from_file_5():
    grep = Grep(['-i', '-w', 'hello', grep_test_1_src])
    assert grep.execute() == 'hello world\nHellO!\n'


def test_from_file_6():
    grep = Grep(['-A','2', '-i', 'hell', grep_test_1_src])
    assert grep.execute() == 'hello world\n\ngo to hell\n--\nHellO!\n'


def test_from_multiple_files_2():
    grep = Grep(['-w', '-i', 'hell', grep_test_1_src, grep_test_2_src])
    assert grep.execute() == f'{grep_test_1_src}:go to hell\n' \
                             f'{grep_test_2_src}:hell hel\n' \
                             f'{grep_test_2_src}:hello hell\n'


def test_with_file_and_data():
    grep = Grep(['hell', grep_test_1_src])
    assert grep.execute('hell') == 'hello world\ngo to hell\n'


def test_grep_no_such_file():
    grep = Grep(['-w', '-i', 'hell', resources_src, grep_test_src])
    sys.stderr = StringIO()
    assert grep.execute() == ''
    assert sys.stderr.getvalue() == f'grep: {resources_src}: is a directory\n' \
                                    f'grep: {grep_test_src}: no such file or directory\n'
