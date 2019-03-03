from .command import Command
import os
import sys


class Wc(Command):
    """
    Class represents `wc' command from bash. Displays the number of lines, words,
    and bytes contained in each input file.
    """
    def __init__(self, args: list):
        super().__init__(args)

    @staticmethod
    def _get_statistics(src, from_file: bool):
        if from_file:
            text = src.read()
            cnt_bytes = os.path.getsize(src.name)
        else:
            text = src
            cnt_bytes = len(text)
        cnt_lines = text.count('\n')
        cnt_words = len(list(filter(lambda w : len(w.strip()) > 0, text.split())))
        return f'{cnt_lines}\t{cnt_words}\t{cnt_bytes}'
    
    def execute(self, data: str = None) -> str:
        """
        Returns the number of lines, words, and bytes contained in each input file,
        or standard input (if no file is specified).
        :param data: string that should be used as an input for this command
        :return: number of lines, words, and bytes in each file, separated by tab characters
        """
        if len(self.args) == 0 and data is not None:
            return self._get_statistics(data, False) + '\n'

        output = ''
        for i, arg in enumerate(self.args):
            if os.path.isfile(arg):
                with open(arg, 'r') as src:
                    output += Wc._get_statistics(src, True)
                    if len(self.args) > 0:
                        output += f'\t{arg}\n'
            elif os.path.isdir(arg):
                sys.stderr.write(f'wc: {arg}: is a directory\n')
            else:
                sys.stderr.write(f'wc: {arg}: no such file or directory\n')

        return output
