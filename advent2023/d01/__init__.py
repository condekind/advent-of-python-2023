# Set with all digits 0-9 as strings
DIGITS = {
    '0',
    '1',
    '2',
    '3',
    '4',
    '5',
    '6',
    '7',
    '8',
    '9',
}


def part_1(lines: list[str]) -> int:
    # The answer is the sum of each line's calibration values. We start with 0
    result = 0

    # For each line
    for ln in lines:
        # We start with an empty string (to construct our 2-digit number)
        num_str = ''

        # We look at each character from the line, from left to right
        for ch in ln:
            # If we find a digit, we add it to num_str and stop
            if ch in DIGITS:
                num_str += ch
                break

        # We look again at each character, this time from right to left
        for ch in ln[::-1]:
            # If we find a digit, we add it to num_str and stop
            if ch in DIGITS:
                num_str += ch
                break

        # We convert the value to a base 10 int and add it to the final result
        result += int(num_str, 10)

    return result


def part_2(lines: list[str]):
    raise NotImplementedError
