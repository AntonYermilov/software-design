from cli.env import Environment
from cli.cli import CommandLineInterpreter
from cli.command.echo import Echo
from cli.command.cat import Cat
from cli.command.pwd import Pwd
from cli.command.wc import Wc
from cli.command.exit import Exit


def init_standard_env():
    return Environment(
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


def init_standard_cli():
    return CommandLineInterpreter(init_standard_env())
