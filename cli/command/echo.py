from .command import Command


class Echo(Command):
    """
    Class represents `echo' command from bash. Writes any specified operands, separated
    by single blank (` ') characters and followed by a newline (`\n') character, to the
    standard output.
    """
    def __init__(self, args: list):
        super().__init__(args)

    def execute(self, data: str = None) -> str:
        """
        Returns command arguments separated by blank characters.
        :param data: string that should be used as an input for this command; ignored by this command
        :return: arguments passed to the command, separated by blank characters
        """
        return ' '.join(map(str, self.args)) + '\n'

