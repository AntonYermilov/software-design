from .command import Command
import sys


class Exit(Command):
    """
    Class represents `exit' command from bash. Terminates CLI.
    """
    def __init__(self, args: list):
        super().__init__(args)

    def execute(self, data: str = None):
        """
        Exits from command line interpreter.
        :param data: string that should be used as an input for this command; ignored by this command
        """
        sys.exit(0)
