from .cli import CommandLineInterpreter
from .env import Environment
from cli.command.wc import Wc
from cli.command.cat import Cat
from cli.command.echo import Echo
from cli.command.pwd import Pwd
from cli.command.grep import Grep
from cli.command.exit import Exit
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
    'grep': Grep,
    'exit': Exit,
}

CLI = CommandLineInterpreter(
    environment=Environment(
        commands=_commands,
        variables=_variables
    )
)
