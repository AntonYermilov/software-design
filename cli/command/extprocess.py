import subprocess
from .command import Command
import sys

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
            sys.stderr.write(f'{self.command}: command not found\n')
            return ''
        return proc.stdout.decode('utf-8')
