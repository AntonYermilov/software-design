import sys
import os
from cli import CLI


def get_current_dir():
    home = CLI.environment.get_variable('HOME')
    working_dir = CLI.environment.get_variable('PWD')
    if working_dir.find(home) == 0 and (len(home) == len(working_dir) or working_dir[len(home)] == os.sep):
        working_dir = working_dir.replace(home, '~')
    return working_dir


def run():
    while True:
        try:
            sys.stdout.write(f'{get_current_dir()}$ ')
            sys.stdout.flush()

            input = sys.stdin.readline()[:-1]
            output = CLI.execute(input)
            sys.stdout.write(output)
        except KeyboardInterrupt:
            sys.stdout.write('\n')


if __name__ == '__main__':
    run()
