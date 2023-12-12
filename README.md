
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
python -m venv .venv
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

Implement the solution to day N on `advent2023/dN/__init__.py`. Days 1-9 have a leading 0 as padding, but that 0 should not be provided on the CLI, as shown below.

If you're using the recommended `pyenv`+`Poetry` setup, and you have activated your virtualenv (e.g., `source .venv/bin/activate`), run:

```bash
python advent2023 --day 1 --part 1 input/d01/part1_example.txt
```

If you prefer, you can instead redirect the input from stdin, e.g.:

```bash
python advent2023 --day 1 --part 1 < input/d01/part1_example.txt
```

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
