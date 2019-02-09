from cli.env import Environment
from cli.cli import CommandLineInterpreter
from cli import _variables, _commands


def init_standard_env():
    return Environment(
        commands=_commands.copy(),
        variables=_variables.copy(),
    )


def init_standard_cli():
    return CommandLineInterpreter(init_standard_env())
