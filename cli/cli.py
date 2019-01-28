#!/usr/bin/env python3

from command import get_command
import sys

def read_command():
    line = sys.stdin.readline()
    args = list(filter(lambda arg: len(arg) > 0, line.strip().split()))
    if len(args) == 0:
        return None
    return get_command(args[0], args[1:])
 

def run():
    while True:
        try:
            sys.stdout.write('$ ')
            sys.stdout.flush()
            command = read_command()
            if command is None:
                continue
            sys.stdout.write(command.execute() + '\n')
        except KeyboardInterrupt:
            sys.stdout.write('\n')
            pass


if __name__ == '__main__':
    run()

