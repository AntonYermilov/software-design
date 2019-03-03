from cli.command.echo import Echo


def test_empty():
    echo = Echo([])
    assert echo.execute() == '\n'


def test_one_argument_1():
    echo = Echo(['hello'])
    assert echo.execute() == 'hello\n'


def test_one_argument_2():
    echo = Echo(['world'])
    assert echo.execute() == 'world\n'


def test_two_arguments():
    echo = Echo(['hello', 'world'])
    assert echo.execute() == 'hello world\n'


def test_many_arguments():
    echo = Echo(['arg1', 'arg2', 'arg3', '...', 'argN', ' arg with spaces '])
    assert echo.execute() == 'arg1 arg2 arg3 ... argN  arg with spaces \n'


def test_with_data():
    echo = Echo([])
    assert echo.execute('some data') == '\n'


def test_one_argument_1_with_data():
    echo = Echo(['hello'])
    assert echo.execute('some data') == 'hello\n'


def test_one_argument_2_with_data():
    echo = Echo(['world'])
    assert echo.execute('some data') == 'world\n'


def test_two_arguments_with_data():
    echo = Echo(['hello', 'world'])
    assert echo.execute('some data') == 'hello world\n'


def test_many_arguments_with_data():
    echo = Echo(['arg1', 'arg2', 'arg3', '...', 'argN', ' arg with spaces '])
    assert echo.execute('some data') == 'arg1 arg2 arg3 ... argN  arg with spaces \n'
