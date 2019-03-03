# Command Line Interpreter

[![Build Status](https://travis-ci.org/AntonYermilov/software-design.svg?branch=cli)](https://travis-ci.org/AntonYermilov/software-design?branch=cli) [![Coverage Status](https://coveralls.io/repos/github/AntonYermilov/software-design/badge.svg?branch=cli)](https://coveralls.io/github/AntonYermilov/software-design?branch=cli)

SPbHSE Software Design course, Spring '19

## Installation

Python 3.7+ is required.

```
git clone https://github.com/AntonYermilov/software-design
cd software-design
git checkout cli
pip3 install -r requirements.txt
```

## Usage

You can use `cli.py` to run Command Line Interpreter.

Currently we support the following commands:
* `cat` – concatenate and print files
* `echo` – write arguments to the standard output
* `wc` – word, line, character, and byte count
* `pwd` – return working directory name
* `exit` – terminate CLI

Also current implementation of CLI supports pipes, variables and quotes.

### Example
```
$ echo arg1 arg2  arg3
arg1 arg2 arg3
$ echo arg1 arg2 arg3 | wc
2       3       15
$ echo "hello  world!" | cat
hello  world!
$ var1="echo"
$ var2="aba"
$ var3=$var2"c"$var2
$ $var1 $var2 $var3
aba abacaba
```

## License
[MIT](LICENCE)