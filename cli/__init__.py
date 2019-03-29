from .cli import CommandLineInterpreter
from .env import Environment
from .command.cd import Cd
from .command.ls import Ls
from .command.wc import Wc
from .command.cat import Cat
from .command.echo import Echo
from .command.pwd import Pwd
from .command.exit import Exit


_variables = {}

_commands = {
    'wc': Wc,
    'cat': Cat,
    'echo': Echo,
    'pwd': Pwd,
    'cd': Cd,
    'ls': Ls,
    'exit': Exit
}

CLI = CommandLineInterpreter(
    environment=Environment(
        commands=_commands,
        variables=_variables
    )
)
