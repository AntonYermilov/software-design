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
            if i != 0:
                output += '\n'
            if os.path.isfile(arg):
                with open(arg, 'r') as src:
                    output += src.read()[:-1]
            else:
                output += f'cat: {arg}: No such file or directory'
                
        return output

