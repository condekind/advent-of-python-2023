import argparse
import fileinput
import importlib


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
    #   python advent2023 --day 1 --part 1 < input/d01/part1_in00.txt
    # or from provided file, e.g.,
    #   python advent2023 --day 1 --part 1 input/d01/part1_in00.txt
    lines = read_input(args.input_files)

    # Our files always have 2 digits, so days 1-9 have a leading 0 as padding
    day = str(args.day).zfill(2)
    daymodule = importlib.import_module(f'd{day}')

    # Run part 1 or 2 of the day's exercise with the lines read from input
    match args.part:
        case 1:
            print(daymodule.part_1(lines))
        case 2:
            print(daymodule.part_2(lines))
        case _:
            raise Exception('Invalid provided day and/or part!')


if __name__ == '__main__':
    start()
