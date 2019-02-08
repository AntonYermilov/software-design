from .command.extprocess import ExternalProcess
from .command.command import Command


class Environment:
    """
    Class represents environment of command line interpreter. It includes available
    commands and variables.
    """
    def __init__(self, commands: dict = None, variables: dict = None):
        self._commands = commands
        self._variables = variables

    def get_command(self, command_name: str, args: list) -> Command:
        """
        Returns command initialized with specified arguments by its name.
        :param command_name: name of the command we want to execute
        :param args: command arguments
        :return: executable instance of command
        """
        if command_name in self._commands:
            return self._commands[command_name](args)
        return ExternalProcess(command_name, args)

    def set_variable(self, variable_name: str, value: str):
        """
        Adds variable with specified name and value to the environment.
        :param variable_name: name of the variable
        :param value: value of the variable
        """
        self._variables[variable_name] = value

    def get_variable(self, variable_name: str):
        """
        Returns value of the specified variable of empty string if this
        variable does not exist in the environment.
        :param variable_name: name of the variable
        :return: value of the variable
        """
        if variable_name not in self._variables:
            return ''
        return self._variables[variable_name]
