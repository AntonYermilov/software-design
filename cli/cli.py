from .parser import Parser, ParsingError
from .env import Environment


class CommandLineInterpreter:
    """
    Class represents simple command line interpreter which is able to parse input and execute
    specified commands.
    """
    def __init__(self, environment : Environment):
        self.environment = environment

    def execute(self, line: str) -> str:
        """
        Parses specified line and executes commands from it.
        :param line: command to be parsed and executed
        :return: output of the executed command or message that specified command is invalid
        """
        if len(line) == 0 or line.isspace():
            return ''

        try:
            parser = Parser(line, self.environment)
            if parser.is_variable():
                variable = parser.parse_variable()
                self.environment.set_variable(*variable)
                return ''
            else:
                result = None
                pipeline = parser.parse_command()
                for arg in pipeline:
                    command = self.environment.get_command(arg[0], arg[1:])
                    result = command.execute(result)
                return result
        except ParsingError as e:
            return e.message
