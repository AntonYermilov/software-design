from .command import Command
import sys


class Exit(Command):
    def __init__(self, args: list):
        super().__init__(args)

    def execute(self, data: str = None):
        sys.exit(0)


