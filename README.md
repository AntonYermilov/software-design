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
* `grep` – file pattern searcher
* `exit` – terminate CLI

Also current implementation of CLI supports pipes, variables and quotes.

## Command description

#### `cat [file ...]`

The cat utility reads files sequentially, writing them to the standard output.  The file operands are processed in command-line order.

#### `echo [string ...]`

The echo utility writes any specified operands, separated by single blank (\` ') characters and followed by a newline (\`\n') character, to the standard output.

#### `wc [file ...]`

The wc utility displays the number of lines, words, and bytes contained in each input file. A line is defined as a string of characters delimited by a <newline> character. Characters beyond the final <newline> character will not be included in the line count.

#### `pwd`

The pwd utility writes the absolute pathname of the current working directory to the standard output.

#### `grep [-i] [-w] [-A num] pattern [file ...]`

The grep utility searches any given input files, selecting lines that match one or more patterns.  By default, a pattern matches an input line if the regular expression (RE) in the pattern matches the input line without its trailing newline.  An empty expression matches every line.  Each input line that matches at least one of the patterns is written to the standard output.

The following options are available:

```
-A num, --after-context=num
             Print num lines of trailing context after each match.
-i, --ignore-case
             Perform case insensitive matching.  By default, grep is case sensitive.
-w, --word-regexp
             The expression is searched for as a word (as if surrounded by `[[:<:]]' and `[[:>:]]')
```

#### `exit`

The exit utility terminates CLI.

## Examples
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
