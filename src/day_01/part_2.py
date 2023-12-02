"""
This module contains functions to solve the calibration value problem.

The calibration value problem involves calculating the sum of calibration values from an input file.
The calibration values are obtained by extracting
numbers or words representing numbers from the input string.

The main functions in this module are:
- get_calibration_value: Calculates the calibration value based on the input string.
- solve: Solves the problem by calculating the sum of calibration values from the input file.

"""

import re
from common import file_reader


def get_calibration_value(input_string):
    """
    Calculates the calibration value based on the input string.

    Args:
        input_string (str): The input string containing numbers or words representing numbers.

    Returns:
        int: The calculated calibration value.

    """
    pattern = re.compile(
        r"(?=(one|two|three|four|five|six|seven|eight|nine|\d))", re.IGNORECASE
    )
    matches = pattern.findall(input_string)

    if not matches:
        return None

    # Convert the first and last matches to integers
    first_match = (
        int(matches[0])
        if matches[0].isdigit()
        else int(
            {
                "one": 1,
                "two": 2,
                "three": 3,
                "four": 4,
                "five": 5,
                "six": 6,
                "seven": 7,
                "eight": 8,
                "nine": 9,
            }[matches[0].lower()]
        )
    )
    last_match = (
        int(matches[-1])
        if matches[-1].isdigit()
        else int(
            {
                "one": 1,
                "two": 2,
                "three": 3,
                "four": 4,
                "five": 5,
                "six": 6,
                "seven": 7,
                "eight": 8,
                "nine": 9,
            }[matches[-1].lower()]
        )
    )

    # Concatenate the first and last matches and return the result
    concatenated_result = int(f"{first_match}{last_match}")

    return concatenated_result


def solve():
    """
    Solves the problem by calculating the sum of calibration values from the input file.

    """
    result = 0

    # Iterate through each line and add the calibration value to the sum
    for line in file_reader.read_input_file(__file__):
        result += get_calibration_value(line)

    # Print the sum
    print(result)
