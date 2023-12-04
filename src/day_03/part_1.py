""" Part 1 of day 3 of Advent of Code 2020. """
from common import file_reader

matrix = []


def is_active_number(number, first_occurence):
    """
    Checks if a given number is active in the matrix.

    Args:
        number (str): The number to check.
        first_occurence (tuple): The coordinates of
            the first occurrence of the number in the matrix.

    Returns:
        bool: True if the number is active, False otherwise.
    """
    for i in range(first_occurence[0] - 1, first_occurence[0] + 2):
        for j in range(first_occurence[1] - 1, first_occurence[1] + len(number) + 1):
            if 0 <= i < len(matrix) and 0 <= j < len(matrix[i]):
                if not matrix[i][j].isdigit() and not matrix[i][j] == ".":
                    return True
    return False


def solve():
    """
    Solve the problem by iterating over the matrix and finding active numbers.
    """
    result = 0

    for row in file_reader.read_input_file(__file__):
        matrix.append(list(row.strip()))

    possible_number = ""
    found_digits = False
    first_occurence = (0, 0)

    for i, row in enumerate(matrix):
        if found_digits and is_active_number(possible_number, first_occurence):
            result += int(possible_number)

        possible_number = ""
        found_digits = False
        first_occurence = (0, 0)

        for j, cell in enumerate(row):
            if cell.isdigit():
                possible_number += cell
                if not found_digits:
                    first_occurence = (i, j)
                found_digits = True
            elif found_digits:
                if is_active_number(possible_number, first_occurence):
                    result += int(possible_number)
                found_digits = False
                possible_number = ""
                first_occurence = (0, 0)

    print(result)
