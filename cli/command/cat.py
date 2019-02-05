from .command import Command
import os


class Cat(Command):
    def __init__(self, args: list):
        super().__init__(args)

    def execute(self, data: str = None) -> str:
        if len(self.args) == 0 and data is not None:
            return data

        output = ''
        for i, arg in enumerate(self.args):
            if os.path.isfile(arg):
                with open(arg, 'r') as src:
                    output += src.read()
            elif os.path.isdir(arg):
                output += f'cat: {arg}: is a directory\n'
            else:
                output += f'cat: {arg}: no such file or directory\n'
                
        return output
