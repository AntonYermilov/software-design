import os

from .command import Command


class Ls(Command):
    """
    Class represents `ls' command from bash. Prints a filename if a file was given and
    a list of files inside the specified directory otherwise.
    """

    def __init__(self, args: list):
        super().__init__(args)

    def execute(self, data: str = None) -> str:
        """
        Returns a list of files, or a filename, or an empty string if a given path doesn't exist.
        :param data: piped input for this command
        """

        if len(self.args) > 1:
            return 'ls: 0 or 1 argument expected\n'
        elif len(self.args) == 1:
            path = self.args[0]
        elif data is not None:
            path = data
        else:
            from cli import CLI
            path = CLI.environment.get_variable('PWD')

        if os.path.isfile(path):
            return os.path.realpath(path) + '\n'

        if os.path.isdir(path):
            return '\n'.join(os.listdir(path)) + '\n'

        return f'ls: {path}: no such file or directory\n'
