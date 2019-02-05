from cli.command.exit import Exit
import pytest


def test_exit_no_args():
    with pytest.raises(SystemExit):
        Exit([]).execute()


def test_exit_with_args():
    with pytest.raises(SystemExit):
        Exit(['hello', 'world']).execute()


def test_exit_with_data():
    with pytest.raises(SystemExit):
        Exit([]).execute('hello world')


def test_exit_with_data_and_args():
    with pytest.raises(SystemExit):
        Exit(['hello', 'world']).execute('hello world')
