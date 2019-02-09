import subprocess
from .command import Command, CommandExecutionError


class ExternalProcess(Command):
    """
    Class represents the shell over external commands, not implemented in CLI.
    """
    def __init__(self, command: str, args: list):
        """
        :param command: name of the external command
        :param args: arguments to be passed to the external command
        """
        super().__init__(args)
        self.command = command

    def execute(self, data: str = None) -> str:
        """
        Executes external command. May use specified string as an input.
        :param data: string that should be used as an input for this command
        :return: string representation of external command output
        """
        try:
            if data is None:
                proc = subprocess.run([self.command, *self.args], stdout=subprocess.PIPE)
            else:
                proc = subprocess.run([self.command, *self.args], stdout=subprocess.PIPE, input=data.encode('utf-8'))
        except FileNotFoundError:
            raise CommandNotFoundError(self.command)
        return proc.stdout.decode('utf-8')


class CommandNotFoundError(CommandExecutionError):
    """
    Class represents error that occur in case no external command with specified name was found
    """
    def __init__(self, command: str):
        super().__init__(f'{command}: command not found\n')
