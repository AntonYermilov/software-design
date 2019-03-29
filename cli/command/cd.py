import os

from cli.command.command import CommandExecutionError
from .command import Command


class Cd(Command):
    """
    Class represents `cd' command from bash. Changes current directory if provided with a correct path to it.
    """

    def __init__(self, args: list):
        super().__init__(args)

    def execute(self, data: str = None) -> str:
        """
        Changes current directory to a new path or home directory if no argument given.
        :param data: piped input for this command; ignored by this command
        :returns empty string or error message
        """
        from cli import CLI

        if len(self.args) >= 1:
            new_path = self.args[0]
        else:
            new_path = os.path.expanduser('~')

        current_path = os.getcwd()
        realpath = os.path.realpath(os.path.join(current_path, new_path))
        if os.path.isdir(realpath):
            os.chdir(realpath)
            return ''
        else:
            raise CommandExecutionError(f'cd: {new_path}: not a directory\n')
