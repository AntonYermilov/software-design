from .command import Command
import os
import sys

class Cat(Command):
    """
    Class represents `cat' command from bash. Reads files sequentially, writing them
    to the standard output.
    """
    def __init__(self, args: list):
        super().__init__(args)

    def execute(self, data: str = None) -> str:
        """
        Returns concatenated content of files passed as arguments to the command. If command
        receives some string as data and no arguments were provided, returns this string.
        :param data: string that should be used as an input for this command; None if
        standard input should be used
        :return: content of the specified files
        """
        if len(self.args) == 0 and data is not None:
            return data

        output = ''
        for i, arg in enumerate(self.args):
            if os.path.isfile(arg):
                with open(arg, 'r') as src:
                    output += src.read()
            elif os.path.isdir(arg):
                sys.stderr.write(f'cat: {arg}: is a directory\n')
            else:
                sys.stderr.write(f'cat: {arg}: no such file or directory\n')
                
        return output
