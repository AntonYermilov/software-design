from cli.parser import Parser, QuoteError, UnexpectedTokenError
from cli.env import Environment
from cli.expression import _Pipeline, _Assignment
import pytest


def test_double_quotes_single_argument():
    command = '"echo"'
    parser = Parser(command, Environment())
    assert parser._parse_pipeline().pipeline == [['echo']]


def test_double_quotes_multiple_arguments():
    command = '"echo arg1 arg2   arg3"'
    parser = Parser(command, Environment())
    assert parser._parse_pipeline().pipeline == [['echo arg1 arg2   arg3']]


def test_single_quotes_single_argument():
    command = '\'echo\''
    parser = Parser(command, Environment())
    assert parser._parse_pipeline().pipeline == [['echo']]


def test_single_quotes_multiple_arguments():
    command = '\'echo arg1 arg2   arg3\''
    parser = Parser(command, Environment())
    assert parser._parse_pipeline().pipeline == [['echo arg1 arg2   arg3']]


def test_double_quotes_escaping():
    command = '"echo \\\\ \\"echo\\" \\a"'
    parser = Parser(command, Environment())
    assert parser._parse_pipeline().pipeline == [['echo \\ "echo" \\a']]


def test_single_quotes_escaping():
    command = '\'echo \\\\ \\"echo\\" \\a\''
    parser = Parser(command, Environment())
    assert parser._parse_pipeline().pipeline == [['echo \\\\ \\"echo\\" \\a']]


def test_no_matching_double_quote():
    command = '"echo\\"\''
    parser = Parser(command, Environment())
    with pytest.raises(QuoteError):
        parser._parse_pipeline()


def test_no_matching_single_quote():
    command = '\'echo"'
    parser = Parser(command, Environment())
    with pytest.raises(QuoteError):
        parser._parse_pipeline()


def test_without_quotes():
    command = 'exit'
    parser = Parser(command, Environment())
    assert parser._parse_pipeline().pipeline == [['exit']]


def test_quotes_union():
    command = '"ec"\'ho\''
    parser = Parser(command, Environment())
    assert parser._parse_pipeline().pipeline == [['echo']]


def test_multiple_commands_without_quotes():
    command = ' echo  arg1   arg2    arg3     '
    parser = Parser(command, Environment())
    assert parser._parse_pipeline().pipeline == [['echo', 'arg1', 'arg2', 'arg3']]


def test_multiple_commands_with_quotes():
    command = ' "echo"  \'arg1\'   "arg"\'2\'    arg3     '
    parser = Parser(command, Environment())
    assert parser._parse_pipeline().pipeline == [['echo', 'arg1', 'arg2', 'arg3']]


def test_one_pipe_with_spaces():
    command = 'echo arg | cat'
    parser = Parser(command, Environment())
    assert parser._parse_pipeline().pipeline == [['echo', 'arg'], ['cat']]


def test_one_pipe_without_spaces():
    command = 'echo arg|cat'
    parser = Parser(command, Environment())
    assert parser._parse_pipeline().pipeline == [['echo', 'arg'], ['cat']]


def test_multiple_pipes():
    command = 'echo arg | cat | wc | wc | wc | cat'
    parser = Parser(command, Environment())
    assert parser._parse_pipeline().pipeline == [['echo', 'arg'], ['cat'], ['wc'], ['wc'], ['wc'], ['cat']]


def test_pipe_in_the_beginning():
    command = '| echo arg | cat | wc | wc | wc | cat'
    parser = Parser(command, Environment())
    with pytest.raises(UnexpectedTokenError):
        parser._parse_pipeline()


def test_pipe_in_the_end():
    command = 'echo arg | cat | wc | wc | wc | cat |'
    parser = Parser(command, Environment())
    with pytest.raises(UnexpectedTokenError):
        parser._parse_pipeline()


def test_double_pipe():
    command = 'echo arg | cat | | wc | wc | wc | cat'
    parser = Parser(command, Environment())
    with pytest.raises(UnexpectedTokenError):
        parser._parse_pipeline()


def test_backslash():
    command = '\\echo \\arg \\\\ \\" \\\' \\| \\ '
    parser = Parser(command, Environment())
    assert parser._parse_pipeline().pipeline == [['echo', 'arg', '\\', '"', '\'', '|', ' ']]


def test_backslash_in_the_end():
    command = 'echo \\'
    parser = Parser(command, Environment())
    with pytest.raises(UnexpectedTokenError):
        parser._parse_pipeline()


def test_variable_substitution():
    environment = Environment(variables={'a': 'b'})
    command = 'echo $a'
    parser = Parser(command, environment)
    assert parser._parse_pipeline().pipeline == [['echo', 'b']]


def test_variable_substitution_double_quotes():
    environment = Environment(variables={'a': 'b'})
    command = 'echo "$a"'
    parser = Parser(command, environment)
    assert parser._parse_pipeline().pipeline == [['echo', 'b']]


def test_variable_substitution_single_quotes():
    environment = Environment(variables={'a': 'b'})
    command = 'echo \'$a\''
    parser = Parser(command, environment)
    assert parser._parse_pipeline().pipeline == [['echo', '$a']]


def test_is_assignment_1():
    command = 'a=b'
    parser = Parser(command, Environment())
    assert parser._is_assignment()


def test_is_assignment_2():
    command = 'CURRENT_DIR="software-design"'
    parser = Parser(command, Environment())
    assert parser._is_assignment()


def test_is_not_assignment_1():
    command = 'echo'
    parser = Parser(command, Environment())
    assert not parser._is_assignment()


def test_is_not_assignment_2():
    command = 'a='
    parser = Parser(command, Environment())
    assert not parser._is_assignment()


def test_is_not_assignment_3():
    command = '"a=b"'
    parser = Parser(command, Environment())
    assert not parser._is_assignment()


def test_is_not_assignment_4():
    command = '"a= b"'
    parser = Parser(command, Environment())
    assert not parser._is_assignment()


def test_parse_assignment():
    command = 'a=b'
    parser = Parser(command, Environment())
    assert parser._parse_assignment().assignment == ['a', 'b']


def test_parse_assignment_with_substitution():
    command = 'a=$b'
    environment =  Environment(variables={'b': 'c'})
    parser = Parser(command, environment)
    assert parser._parse_assignment().assignment == ['a', 'c']


def test_parse_assignment_with_double_quotes():
    command = 'a="$b"'
    environment =  Environment(variables={'b': 'c'})
    parser = Parser(command, environment)
    assert parser._parse_assignment().assignment == ['a', 'c']


def test_parse_assignment_with_single_quotes():
    command = 'a=\'$b\''
    environment =  Environment(variables={'b': 'c'})
    parser = Parser(command, environment)
    assert parser._parse_assignment().assignment == ['a', '$b']


def test_parse_expression_pipeline():
    command = 'echo a | cat'
    environment = Environment()
    parser = Parser(command, environment)
    assert isinstance(parser.parse(), _Pipeline)


def test_parse_expression_assignment():
    command = 'a="b"c'
    environment = Environment()
    parser = Parser(command, environment)
    assert isinstance(parser.parse(), _Assignment)


def test_parse_incorrect_assignment_with_pipe():
    command = 'a=b| '
    environment = Environment()
    parser = Parser(command, environment)
    with pytest.raises(UnexpectedTokenError):
        parser._parse_assignment()


def test_parse_incorrect_assignment_with_backslash():
    command = 'a=b\\'
    environment = Environment()
    parser = Parser(command, environment)
    with pytest.raises(UnexpectedTokenError):
        parser._parse_assignment()


def test_parse_incorrect_assignment_with_multiple_args():
    command = 'a=b c'
    environment = Environment()
    parser = Parser(command, environment)
    with pytest.raises(UnexpectedTokenError):
        parser._parse_assignment()