from .command import Command
import os


class Wc(Command):
    def __init__(self, args: list):
        super().__init__(args)

    @staticmethod
    def get_statistics(text: str, from_file: bool):
        cnt_lines = text.count('\n') + (0 if from_file else 1)
        cnt_words = len(list(filter(lambda w : len(w.strip()) > 0, text.split())))
        cnt_bytes = len(text)
        return f'{cnt_lines}\t{cnt_words}\t{cnt_bytes}'
    
    def execute(self, data: str = None) -> str:
        if len(self.args) == 0 and data is not None:
            return self.get_statistics(data, False) + '\n'

        output = ''
        for i, arg in enumerate(self.args):
            if os.path.isfile(arg):
                with open(arg, 'r') as src:
                    text = src.read()
                    output += Wc.get_statistics(text, True)
                    if len(self.args) > 0:
                        output += f'\t{arg}\n'
            elif os.path.isdir(arg):
                output += f'wc: {arg}: is a directory\n'
            else:
                output += f'wc: {arg}: no such file or directory\n'

        return output
