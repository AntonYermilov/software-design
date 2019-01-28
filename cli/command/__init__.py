from .wc import Wc
from .cat import Cat
from .echo import Echo
from .pwd import Pwd
from .exit import Exit
from .extprocess import ExternalProcess

_commands = {
    'wc': Wc,
    'cat': Cat,
    'echo': Echo,
    'pwd': Pwd,
    'exit': Exit,
}


def get_command(command_name: str, args: list):
    if command_name in _commands:
        return _commands[command_name](args)
    return ExternalProcess(command_name, args)

