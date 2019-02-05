from .command.extprocess import ExternalProcess


class Environment:
    def __init__(self, commands: dict = None, variables: dict = None):
        self._commands = commands
        self._variables = variables

    def get_command(self, command_name: str, args: list):
        if command_name in self._commands:
            return self._commands[command_name](args)
        return ExternalProcess(command_name, args)

    def set_variable(self, variable_name: str, value: str):
        self._variables[variable_name] = value

    def get_variable(self, variable_name: str):
        if variable_name not in self._variables:
            return ''
        return self._variables[variable_name]
