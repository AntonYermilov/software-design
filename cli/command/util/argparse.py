import argparse
from cli.command.command import CommandExecutionError

class CommandArgumentParser(argparse.ArgumentParser):
    """
    Class overrides standard ArgumentParser functions in order to suppress standard output and
    not to exit from CLI.
    """
    def error(self, message):
        """
        Raises CommandArgumentParsingError exception, initialized with the error description message.
        """
        message = f'{self.format_usage()}{self.prog}: {message}\n'
        raise CommandArgumentParsingError(message)


class CommandArgumentParsingError(CommandExecutionError):
    """
    Class represents error that may be thrown in case command received
    unknown options.
    """
    def __init__(self, message):
        super().__init__(message)
