from cli.command.grep import Grep
from cli.command.util.argparse import CommandArgumentParsingError
import pytest


def test_no_arguments():
    with pytest.raises(CommandArgumentParsingError):
        Grep([])


def test_invalid_arguments():
    with pytest.raises(CommandArgumentParsingError):
        Grep(['-i', '-j', 'pattern', 'file'])


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
    with pytest.raises(CommandArgumentParsingError):
        Grep(['-A', 'a', 'aca'])


def test_from_file_1():
    grep = Grep(['hello', 'tests/resources/grep_test_1.txt'])
    assert grep.execute() == 'hello world\n'


def test_from_file_2():
    grep = Grep(['hell', 'tests/resources/grep_test_1.txt'])
    assert grep.execute() == 'hello world\ngo to hell\n'


def test_from_file_3():
    grep = Grep(['-w', 'hell', 'tests/resources/grep_test_1.txt'])
    assert grep.execute() == 'go to hell\n'


def test_from_file_4():
    grep = Grep(['-i', 'hell', 'tests/resources/grep_test_1.txt'])
    assert grep.execute() == 'hello world\ngo to hell\nHellO!\n'


def test_from_file_5():
    grep = Grep(['-i', '-w', 'hello', 'tests/resources/grep_test_1.txt'])
    assert grep.execute() == 'hello world\nHellO!\n'


def test_from_file_6():
    grep = Grep(['-A','2', '-i', 'hell', 'tests/resources/grep_test_1.txt'])
    assert grep.execute() == 'hello world\n\ngo to hell\n--\nHellO!\n'


def test_from_multiple_files_2():
    grep = Grep(['-w', '-i', 'hell', 'tests/resources/grep_test_1.txt',
                 'tests/resources/grep_test_2.txt'])
    assert grep.execute() == 'tests/resources/grep_test_1.txt:go to hell\n' \
                             'tests/resources/grep_test_2.txt:hell hel\n' \
                             'tests/resources/grep_test_2.txt:hello hell\n'


def test_with_file_and_data():
    grep = Grep(['hell', 'tests/resources/grep_test_1.txt'])
    assert grep.execute('hell') == 'hello world\ngo to hell\n'


def test_grep_no_such_file():
    grep = Grep(['-w', '-i', 'hell', 'tests/resources/',
                 'tests/resources/grep_test.txt'])
    assert grep.execute() == 'grep: tests/resources/: is a directory\n' \
                             'grep: tests/resources/grep_test.txt: no such file or directory\n'
