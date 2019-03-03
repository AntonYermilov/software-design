from abc import ABC, abstractmethod
from .env import Environment


class Expression(ABC):
    def __init__(self, environment: Environment):
        self.environment = environment

    @abstractmethod
    def execute(self) -> str:
        pass


class _Pipeline(Expression):
    def __init__(self, environment: Environment, pipeline: list):
        super().__init__(environment)
        self.pipeline = pipeline

    def execute(self) -> str:
        result = None
        for arg in self.pipeline:
            command = self.environment.get_command(arg[0], arg[1:])
            result = command.execute(result)
        return result


class _Assignment(Expression):
    def __init__(self, environment: Environment, assignment: list):
        super().__init__(environment)
        self.assignment = assignment

    def execute(self) -> str:
        self.environment.set_variable(*self.assignment)
        return ''