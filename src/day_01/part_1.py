"""
This module contains functions to solve the puzzle for Day 1, Part 1 of Advent of Code 2023.

The puzzle involves calculating the calibration value for each line in an input file and
printing the sum of all calibration values.

The module includes the following functions:
- get_calibration_value: Calculates the calibration value for a given line.
- solve: Solves the puzzle by calculating the calibration value for each line in the input file
    and printing the sum of all calibration values.
"""

from common import file_reader


def get_calibration_value(line):
    """
    Calculates the calibration value for a given line.

    Parameters:
    line (str): The input line containing digits.

    Returns:
    int: The calibration value calculated from the first and last digits of the line.
    """
    return int(
        "".join(filter(str.isdigit, line))[0] + "".join(filter(str.isdigit, line))[-1]
    )


def solve():
    """
    Solves the puzzle by calculating the calibration value for each line in the input file
    and printing the sum of all calibration values.
    """
    result = 0

    # Iterate through each line and add the calibration value to the result
    for line in file_reader.read_input_file(__file__):
        result += get_calibration_value(line)

    # Print the result
    print(result)
