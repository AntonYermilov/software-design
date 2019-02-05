import sys
from .parser import Parser, ParsingError
from .env import Environment


class CommandLineInterpreter:
    def __init__(self, environment : Environment):
        self.environment = environment

    def run(self):
        while True:
            try:
                sys.stdout.write('$ ')
                sys.stdout.flush()

                input = sys.stdin.readline()[:-1]
                output = self._execute(input)
                sys.stdout.write(output)

            except KeyboardInterrupt:
                sys.stdout.write('\n')
            except ParsingError as e:
                sys.stdout.write(e.message)

    def _execute(self, line: str) -> str:
        if line.isspace():
            return ''

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
