from .command import Command
import os


class Pwd(Command):
    def __init__(self, args: list):
        super().__init__(args)

    def execute(self, data: str = None) -> str:
        return os.getcwd() + '\n'
