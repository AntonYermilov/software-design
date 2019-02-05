from .cli import CommandLineInterpreter
from .env import Environment
from .command.wc import Wc
from .command.cat import Cat
from .command.echo import Echo
from .command.pwd import Pwd
from .command.exit import Exit


CLI = CommandLineInterpreter(
    environment=Environment(
        commands={
            'wc': Wc,
            'cat': Cat,
            'echo': Echo,
            'pwd': Pwd,
            'exit': Exit,
        },
        variables={
        }
    )
)