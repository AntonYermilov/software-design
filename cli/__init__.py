from .cli import CommandLineInterpreter
from .env import Environment
from .command.wc import Wc
from .command.cat import Cat
from .command.echo import Echo
from .command.pwd import Pwd
from .command.exit import Exit
import os


_variables = {
    'PWD': os.getcwd(),
    'HOME': os.path.expanduser('~')
}

_commands = {
    'wc': Wc,
    'cat': Cat,
    'echo': Echo,
    'pwd': Pwd,
    'exit': Exit,
}

CLI = CommandLineInterpreter(
    environment=Environment(
        commands=_commands,
        variables=_variables
    )
)
