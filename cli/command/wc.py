from .command import Command
import os


class Wc(Command):
    def __init__(self, args: list):
        super().__init__(args)

    def get_statistics(self, text):
        cnt_lines = len(text.split('\n')) - 1
        cnt_words = len(list(filter(lambda w : len(w.strip()) > 0, text.split(' '))))
        cnt_bytes = len(text)
        return f'{cnt_lines}\t{cnt_words}\t{cnt_bytes}'
    
    def execute(self, data: str = None) -> str:
        if len(self.args) == 0 and data is not None:
            return self.get_statistics(data)

        output = ''
        for i, arg in enumerate(self.args):
            if i != 0:
                output += '\n'
            if os.path.isfile(arg):
                with open(arg, 'r') as src:
                    text = src.read()
                    output += self.get_statistics(text)
                    if len(self.args) > 0:
                        output += f'\t{arg}'
            else:
                output += f'wc: {arg}: No such file or directory'

        return output

