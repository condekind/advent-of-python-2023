import sys
import argparse
import fileinput
import importlib
import importlib.util
from pathlib import Path

_basemodname = Path(__file__).parent.name


def read_input(input_files):
    """Reads input file and returns a list[str], one str per non-empty line"""

    lines: list[str] = []

    # Use fileinput to read either from the list of files or stdin
    with fileinput.input(
        files=input_files if input_files else ('-',), encoding='utf-8'
    ) as f:
        for line in f:
            # Remove leading and trailing whitespaces
            ln = line.strip()

            # If the resulting string is not empty, add it to lines
            if len(ln) > 0:
                lines.append(ln)

    return lines


def start():
    """
    Parses command line options/arguments, calls read_input, then invokes the
    function part_1(...) or part_2(...) that matches the provided day/part
    """

    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-d',
        '--day',
        type=int,
        help='Define which day of the calendar to run',
        choices=list(range(1, 26)),
        required=True,
    )
    parser.add_argument(
        '-p',
        '--part',
        type=int,
        help='Define which part of the exercise to run',
        choices=[1, 2],
        required=True,
    )
    parser.add_argument('input_files', nargs='*', help='Input file(s)')
    args = parser.parse_args()

    # Read input from stdin, e.g.,
    #   python advent2042 --day 1 --part 1 < input/d01/part1_in00.txt
    # or from provided file, e.g.,
    #   python advent2042 --day 1 --part 1 input/d01/part1_in00.txt
    lines = read_input(args.input_files)

    # The purpose of this next section is to allow for execution of the project
    # by running either one of:
    #   python3 -m <basemodname> ...
    # or
    #   python3 <basemodname ...
    #
    # The directory for each day always have 2 digits, so days 1-9 have a
    # leading 0 as padding, e.g., day 1 module: d01; day 21 module: d21;
    daymodname = f'd{str(args.day).zfill(2)}'
    if _basemodname in sys.modules:
        daymodule = importlib.import_module(
            f'{_basemodname}.{daymodname}', package=_basemodname
        )
    elif (spec := importlib.util.find_spec(daymodname)) is not None:
        daymodule = importlib.util.module_from_spec(spec)
        sys.modules[daymodname] = daymodule
        if spec.loader is not None:
            spec.loader.exec_module(daymodule)
        else:
            raise ModuleNotFoundError
    else:
        try:
            daymodule = importlib.import_module(
                f'{_basemodname}.{daymodname}', package=_basemodname
            )
        except ModuleNotFoundError as e:
            print(
                f'Module {_basemodname}.{daymodname} could not be found: {e}',
                file=sys.stderr,
            )
            raise

    # Run part 1 or 2 of the day's exercise with the lines read from input
    match args.part:
        case 1:
            print(daymodule.part_1(lines))
        case 2:
            print(daymodule.part_2(lines))
        case other:
            # Should be unreachable since the valid choices were provided to
            # argparse
            raise Exception(f'Invalid part: `--part {other}`')


if __name__ == '__main__':
    start()
