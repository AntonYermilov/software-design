from .command import Command


class Echo(Command):
    def __init__(self, args: list):
        super().__init__(args)

    def execute(self, data: str = None) -> str:
        return ' '.join(map(str, self.args)) + '\n'

