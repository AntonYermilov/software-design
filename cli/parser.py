from .env import Environment


class Parser:
    """
    Class represents parser of command lines.
    """
    def __init__(self, command: str, environment: Environment):
        """
        :param command: command to be parsed
        :param environment: environment that contains information about existing variables
        """
        self.index = 0
        self.command = command
        self.environment = environment

    def is_variable(self) -> bool:
        """
        Checks whether specified command should be parsed as a variable creation or as a
        command execution.
        :return: `True' if command corresponds to variable creation; `False' otherwise
        """
        pos = self.command.find('=')
        if pos == -1 or pos + 1 == len(self.command):
            return False

        correct = True
        for c in self.command[:pos]:
            correct &= c.isalnum() or c == '_'

        return pos != 0 and correct and not self.command[pos + 1].isspace()

    def parse_variable(self) -> list:
        """
        Tries to parse command line as a variable creation.
        :return: list of two elements, first one corresponds to the variable name, second
        one corresponds to the variable value
        :exception ParsingError: if the specified command cannot be parsed because of a
        syntax error
        """
        pos = self.command.find('=')
        name, value = self.command[:pos], self.command[pos + 1:]

        self.index = 0
        args = []

        self._parse_command(value, args)
        if self.index < len(value):
            raise UnexpectedTokenError('|')
        if len(args) > 1:
            raise UnexpectedTokenError(args[1])
        return [name, args[0]]

    def parse_command(self) -> list:
        """
        Tries to parse command line as a command execution.
        :return: a list of commands which were separated by pipes; each command is
        represented as a list of string tokens, first of which is a command name, and
        others are command arguments
        :exception ParsingError: if the specified command cannot be parsed because of a
        syntax error
        """
        self.index = 0
        return self._parse_pipeline(self.command)

    def _parse_pipeline(self, command: str) -> list:
        pipeline = [[]]
        while self.index < len(command):
            self._parse_command(command, pipeline[-1])
            if self.index < len(command):
                pipeline.append([])
                self.index += 1

        for args in pipeline:
            if len(pipeline) > 1 and len(args) == 0:
                raise UnexpectedTokenError('|')
        return pipeline

    def _parse_command(self, command: str, args: list):
        was_space = True
        while self.index < len(command):
            if command[self.index] == '|':
                break

            if command[self.index] == ' ':
                was_space = True
                self.index += 1
                continue

            if was_space:
                was_space = False
                args.append('')

            if command[self.index] == '\'':
                args[-1] += self._parse_single_quotes(command)
                continue
            if command[self.index] == '"':
                args[-1] += self._parse_double_quotes(command)
                continue
            if command[self.index] == '\\':
                if self.index + 1 == len(command):
                    raise UnexpectedTokenError('\\')
                else:
                    args[-1] += command[self.index + 1]
                    self.index += 2
                    continue
            if command[self.index] == '$':
                args[-1] += self._parse_variable(command)
                continue

            args[-1] += command[self.index]
            self.index += 1

    def _parse_single_quotes(self, command: str) -> str:
        result = ''

        self.index += 1
        closed = False
        while self.index < len(command) and not closed:
            if command[self.index] == '\'':
                closed = True
            else:
                result += command[self.index]
            self.index += 1

        if not closed:
            raise QuoteError()
        return result

    def _parse_double_quotes(self, command: str) -> str:
        result = ''

        self.index += 1
        closed = False
        while self.index < len(command) and not closed:
            if command[self.index] == '$':
                result += self._parse_variable(command)
                continue
            if command[self.index] == '\\':
                if self.index + 1 == len(command):
                    raise UnexpectedTokenError('\\')
                elif command[self.index + 1] in '\\\"':
                    result += command[self.index + 1]
                    self.index += 2
                    continue
            if command[self.index] == '"':
                closed = True
            else:
                result += command[self.index]
            self.index += 1

        if not closed:
            raise QuoteError()
        return result

    def _parse_variable(self, command: str) -> str:
        result = ''

        self.index += 1
        while self.index < len(command) and str.isalnum(command[self.index]):
            result += command[self.index]
            self.index += 1

        return '$' if len(result) == 0 else self.environment.get_variable(result)


class ParsingError(Exception):
    """
    Class represents error that may occur during parsing command line.
    """
    def __init__(self, message):
        self.message = message


class UnexpectedTokenError(ParsingError):
    """
    Class represents error that occur in case the line contains some unexpected token.
    This token can be passed to the class constructor.
    """
    def __init__(self, token: str):
        super().__init__(f'cli: syntax error near unexpected token `{token}\'\n')


class QuoteError(ParsingError):
    """
    Class represents error that occur in case single- or double quote mismatch found.
    """
    def __init__(self):
        super().__init__('cli: no matching quote found\n')
