from .command import Command, UnknownOptionError
import os


class Pwd(Command):
    def __init__(self, args: list):
        super().__init__(args)

    def execute(self, data: str = None) -> str:
        if len(self.args) != 0:
            raise UnknownOptionError('Command `pwd` expects no arguments, but some were passed')
        return os.getcwd()

