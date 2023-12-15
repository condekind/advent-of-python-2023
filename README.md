
# Advent of Code 2023

This repository provides boilerplate code so you can jump straight into coding
the challenges from the [advent of code 2023](https://adventofcode.com/2023)

## Optional dependencies (recommended)

- [`pyenv`](https://github.com/pyenv/pyenv)
- [`Poetry`](https://python-poetry.org/)

## Optional setup (recommended)

With pyenv and poetry installed, run the following commands, from the root of the repository, in this order:

1. Install Python 3.12.1 with pyenv:
```bash
pyenv install 3.12.1
```
2. Use pyenv to create a .python-version file that will be used by your shell if you installed pyenv correctly:
```bash
pyenv local 3.12.1
```
3. Create a virtualenv, using the Python version installed above:
```bash
python3 -m venv .venv
```
4. Activate the virtualenv created above:
```bash
source .venv/bin/activate
```
5. Install other dependencies (linter, formatter, etc)
```bash
poetry install
```

> **Obs:** Step #4 is the only one you'll need to repeat (from the root of the repo) after you close your terminal. The previous ones are one time only and the last one should only be repeated if you modify your `pyproject.toml`.

## Usage

Part 1 of the first day is already [implemented](advent2023/d01/__init__.py), to serve as an example.

Implement the solution to day N on `advent2023/dN/__init__.py`. The directory for days 1-9 have a leading 0 as padding, but that 0 should not be provided on the command line, as shown below:

```bash
python3 advent2023 --day 1 --part 1 input/d01/part1_example.txt
```

If you prefer, you can instead redirect the input from stdin, e.g.:

```bash
python3 advent2023 --day 1 --part 1 < input/d01/part1_example.txt
```

**Troubleshooting:**

> The command above does not work!

For the first day, the commands above should work even without pyenv and Poetry. However, using the recommended `pyenv`+`Poetry` setup (remembering to activate your virtualenv, e.g., `source .venv/bin/activate`) decreases the likelihood of conflicts with your version of python available system-wide and its ecosystem.

## Development commands/helpers

If you're using poetry, there are some nice commands to lint, format and clean your files:

```bash
make lint
```

```bash
make fmt
```

```bash
make clean
```

## Extra info for nerds

### How does this repo work?

The entry point for every day/part is [this file](advent2023/__main__.py). It reads the command line options/arguments and additionally, either accepts an input file path directly or reads the input from stdin. It will call either the part_1 or part_2 function of the provided day, which is located in `advent2023/dXX/__init__.py`

### I want to modify the way the input is parsed

In the file mentioned above, the default is to read the input and return a list of strings, one for each line. This might not be desirable for every day of the challenge. Since this repo is only a template to get started with the challenge, the modifications to parse input in a different manner are left as an exercise for the programmer 😉
