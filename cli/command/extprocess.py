import subprocess
from .command import Command


class ExternalProcess(Command):
    def __init__(self, command: str, args: list):
        super().__init__(args)
        self.command = command

    def execute(self, data: str = None) -> str:
        try:
            if data is None:
                proc = subprocess.run([self.command, *self.args], stdout=subprocess.PIPE)
            else:
                proc = subprocess.run([self.command, *self.args], stdout=subprocess.PIPE, input=data.encode('utf-8'))
        except FileNotFoundError:
            return f'{self.command}: command not found\n'
        return proc.stdout.decode('utf-8')
