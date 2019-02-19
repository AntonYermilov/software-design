import os

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
            new_path = CLI.environment.get_variable('HOME')

        current_path = CLI.environment.get_variable('PWD')
        realpath = os.path.realpath(os.path.join(current_path, new_path))
        if os.path.isdir(realpath):
            CLI.environment.set_variable('PWD', realpath)
            return ''
        else:
            return f'cd: {new_path}: not a directory\n'
