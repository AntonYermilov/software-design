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


class CommandExecutionError(Exception):
    """
    Class represent interface for errors that occur while executing commands.
    """
    def __init__(self, message):
        self.message = message
