from abc import ABC, abstractmethod


class Command(ABC):
    """
    Class represents executable command interface.
    """
    def __init__(self, args: list):
        self.args = args

    @abstractmethod
    def execute(self, data: str = None) -> str:
        """
        Executes command with specified arguments. May use string data as an input
        instead of standard input.
        :param data: string that should be used as an input for this command; None if
        standard input should be used
        :return: string representation of the command output
        """
        pass


class UnknownOptionError(Exception):
    def __init__(self, command, option):
        """
        Class represents error that may be thrown in case command received
        unknown options.
        :param command: name of the command that was executed
        :param option: unknown option that was passed to the command as an argument
        """
        self.message = f'{command}: unknown option `{option}\'\n'
