from cli.command.command import Command
from cli.command.util.argparse import CommandArgumentParser, CommandArgumentParsingError
import os
import re
import sys


class Grep(Command):
    """
    Class represents `grep' command from bash. Searches any given input files,
    selecting lines that match one or more patterns.

    Supports such options as:
    -i      perform case insensitive matching
    -w      the expression is searched for as a word
    -A n    print `n' lines of trailing context after each match
    """
    def __init__(self, args: list):
        super().__init__(args)

    def _parse_arguments(self):
        """
        :exception CommandArgumentParsingError: if command received incorrect arguments
        """
        parser = CommandArgumentParser(prog='grep', add_help=False)
        parser.add_argument('-i', '--ignore_case', action='store_true', default=False,
                            help='perform case insensitive matching')
        parser.add_argument('-w', '--word_regex', action='store_true', default=False,
                            help='the expression is searched for as a word')
        parser.add_argument('-A', '--after_context', metavar='N', action='store', type=int, default=0,
                            help='print N lines of trailing context after each match')
        parser.add_argument('pattern', type=str)
        parser.add_argument('file', nargs='*')

        config = parser.parse_args(self.args)

        self.trailing_lines = config.after_context
        self.regex_flag = re.IGNORECASE if config.ignore_case else 0
        self.pattern = config.pattern
        self.files = config.file

        if config.word_regex:
            non_word_symbol = '(^|$|[^a-zA-Z0-9_])'
            self.pattern = f'{non_word_symbol}{self.pattern}{non_word_symbol}'

    def execute(self, data: str = None):
        """
        Searches for a specified in arguments pattern in all input files. Output of the command
        depends on other passed to the command arguments.
        :param data: string that should be used as an input for this command if no files are provided
        :return: lines that match the pattern
        """
        try:
            self._parse_arguments()
        except CommandArgumentParsingError as e:
            sys.stderr.write(e.message)
            return ''

        if len(self.files) == 0 and data is not None:
            return self._find_matchings('', data)

        output = ''
        for i, file in enumerate(self.files):
            if os.path.isfile(file):
                with open(file, 'r') as src:
                    text = src.read()
                    source = f'{file}:' if len(self.files) > 1 else ''
                    output += self._find_matchings(source, text)
            elif os.path.isdir(file):
                sys.stderr.write(f'grep: {file}: is a directory\n')
            else:
                sys.stderr.write(f'grep: {file}: no such file or directory\n')
        return output

    def _find_matchings(self, source: str, data: str):
        if len(data) > 0 and data[-1] == '\n':
            data = data[:-1]

        result = ''
        last_printed_line = -1
        for i, line in enumerate(data.split('\n')):
            if i <= last_printed_line:
                result += f'{source}{line}\n'
                continue
            if re.search(self.pattern, line, flags=self.regex_flag):
                if self.trailing_lines > 0 and last_printed_line != -1 and last_printed_line + 1 < i:
                    result += '--\n'
                last_printed_line = i + self.trailing_lines
                result += f'{source}{line}\n'
        return result
