from abc import ABC, abstractmethod


class Command(ABC):
    def __init__(self, args: list):
        self.args = args

    @abstractmethod
    def execute(self, data: str = None) -> str:
        pass


class UnknownOptionError(Exception):
    def __init__(self, message):
        self.message = message

