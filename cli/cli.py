from .parser import Parser, ParsingError
from .env import Environment


class CommandLineInterpreter:
    def __init__(self, environment : Environment):
        self.environment = environment

    def execute(self, line: str) -> str:
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
