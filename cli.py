import sys
from cli import CLI


def run():
    while True:
        try:
            sys.stdout.write('$ ')
            sys.stdout.flush()

            input = sys.stdin.readline()[:-1]
            output = CLI.execute(input)
            sys.stdout.write(output)
        except KeyboardInterrupt:
            sys.stdout.write('\n')


if __name__ == '__main__':
    run()
