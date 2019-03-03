from .command import Command
import os


class Pwd(Command):
    """
    Class represents `pwd' command from bash. Prints working directory name.
    """
    def __init__(self, args: list):
        super().__init__(args)

    def execute(self, data: str = None) -> str:
        """
        Returns working directory name.
        :param data: string that should be used as an input for this command; ignored by this command
        :return: working directory name
        """
        return os.getcwd() + '\n'
