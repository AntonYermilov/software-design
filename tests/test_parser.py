from cli.parser import Parser, QuoteError, UnexpectedTokenError
from cli.env import Environment
import pytest


def test_double_quotes_single_argument():
    command = '"echo"'
    parser = Parser(command, Environment())
    assert parser.parse_command() == [['echo']]


def test_double_quotes_multiple_arguments():
    command = '"echo arg1 arg2   arg3"'
    parser = Parser(command, Environment())
    assert parser.parse_command() == [['echo arg1 arg2   arg3']]


def test_single_quotes_single_argument():
    command = '\'echo\''
    parser = Parser(command, Environment())
    assert parser.parse_command() == [['echo']]


def test_single_quotes_multiple_arguments():
    command = '\'echo arg1 arg2   arg3\''
    parser = Parser(command, Environment())
    assert parser.parse_command() == [['echo arg1 arg2   arg3']]


def test_double_quotes_escaping():
    command = '"echo \\\\ \\"echo\\" \\a"'
    parser = Parser(command, Environment())
    assert parser.parse_command() == [['echo \\ "echo" \\a']]


def test_single_quotes_escaping():
    command = '\'echo \\\\ \\"echo\\" \\a\''
    parser = Parser(command, Environment())
    assert parser.parse_command() == [['echo \\\\ \\"echo\\" \\a']]


def test_no_matching_double_quote():
    command = '"echo\\"\''
    parser = Parser(command, Environment())
    with pytest.raises(QuoteError):
        parser.parse_command()


def test_no_matching_single_quote():
    command = '\'echo"'
    parser = Parser(command, Environment())
    with pytest.raises(QuoteError):
        parser.parse_command()


def test_without_quotes():
    command = 'exit'
    parser = Parser(command, Environment())
    assert parser.parse_command() == [['exit']]


def test_quotes_union():
    command = '"ec"\'ho\''
    parser = Parser(command, Environment())
    assert parser.parse_command() == [['echo']]


def test_multiple_commands_without_quotes():
    command = ' echo  arg1   arg2    arg3     '
    parser = Parser(command, Environment())
    assert parser.parse_command() == [['echo', 'arg1', 'arg2', 'arg3']]


def test_multiple_commands_with_quotes():
    command = ' "echo"  \'arg1\'   "arg"\'2\'    arg3     '
    parser = Parser(command, Environment())
    assert parser.parse_command() == [['echo', 'arg1', 'arg2', 'arg3']]


def test_one_pipe_with_spaces():
    command = 'echo arg | cat'
    parser = Parser(command, Environment())
    assert parser.parse_command() == [['echo', 'arg'], ['cat']]


def test_one_pipe_without_spaces():
    command = 'echo arg|cat'
    parser = Parser(command, Environment())
    assert parser.parse_command() == [['echo', 'arg'], ['cat']]


def test_multiple_pipes():
    command = 'echo arg | cat | wc | wc | wc | cat'
    parser = Parser(command, Environment())
    assert parser.parse_command() == [['echo', 'arg'], ['cat'], ['wc'], ['wc'], ['wc'], ['cat']]


def test_pipe_in_the_beginning():
    command = '| echo arg | cat | wc | wc | wc | cat'
    parser = Parser(command, Environment())
    with pytest.raises(UnexpectedTokenError):
        parser.parse_command()


def test_pipe_in_the_end():
    command = 'echo arg | cat | wc | wc | wc | cat |'
    parser = Parser(command, Environment())
    with pytest.raises(UnexpectedTokenError):
        parser.parse_command()


def test_double_pipe():
    command = 'echo arg | cat | | wc | wc | wc | cat'
    parser = Parser(command, Environment())
    with pytest.raises(UnexpectedTokenError):
        parser.parse_command()


def test_backslash():
    command = '\\echo \\arg \\\\ \\" \\\' \\| \\ '
    parser = Parser(command, Environment())
    assert parser.parse_command() == [['echo', 'arg', '\\', '"', '\'', '|', ' ']]


def test_backslash_in_the_end():
    command = 'echo \\'
    parser = Parser(command, Environment())
    with pytest.raises(UnexpectedTokenError):
        parser.parse_command()


def test_variable_substitution():
    environment = Environment(variables={'a': 'b'})
    command = 'echo $a'
    parser = Parser(command, environment)
    assert parser.parse_command() == [['echo', 'b']]


def test_variable_substitution_double_quotes():
    environment = Environment(variables={'a': 'b'})
    command = 'echo "$a"'
    parser = Parser(command, environment)
    assert parser.parse_command() == [['echo', 'b']]


def test_variable_substitution_single_quotes():
    environment = Environment(variables={'a': 'b'})
    command = 'echo \'$a\''
    parser = Parser(command, environment)
    assert parser.parse_command() == [['echo', '$a']]


def test_is_variable():
    command = 'a=b'
    parser = Parser(command, Environment())
    assert parser.is_variable()


def test_is_not_variable_1():
    command = 'echo'
    parser = Parser(command, Environment())
    assert not parser.is_variable()


def test_is_not_variable_2():
    command = 'a='
    parser = Parser(command, Environment())
    assert not parser.is_variable()


def test_is_not_variable_3():
    command = '"a=b"'
    parser = Parser(command, Environment())
    assert not parser.is_variable()


def test_is_not_variable_4():
    command = '"a= b"'
    parser = Parser(command, Environment())
    assert not parser.is_variable()


def test_parse_variable():
    command = 'a=b'
    parser = Parser(command, Environment())
    assert parser.parse_variable() == ['a', 'b']


def test_parse_variable_with_substitution():
    command = 'a=$b'
    environment =  Environment(variables={'b': 'c'})
    parser = Parser(command, environment)
    assert parser.parse_variable() == ['a', 'c']


def test_parse_variable_with_double_quotes():
    command = 'a="$b"'
    environment =  Environment(variables={'b': 'c'})
    parser = Parser(command, environment)
    assert parser.parse_variable() == ['a', 'c']


def test_parse_variable_with_single_quotes():
    command = 'a=\'$b\''
    environment =  Environment(variables={'b': 'c'})
    parser = Parser(command, environment)
    assert parser.parse_variable() == ['a', '$b']
