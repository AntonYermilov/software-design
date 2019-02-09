import sys
import re
from cli import CLI


def get_current_dir():
    home = CLI.environment.get_variable('HOME')
    working_dir = CLI.environment.get_variable('PWD')
    regex = f'^{home}[/|$]'
    if re.search(regex, working_dir):
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
