""" Part 1 of day 3 of Advent of Code 2020. """
from common import file_reader

matrix = []


def is_gear_number(number, first_occurence):
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
                if matrix[i][j] == "*":
                    return (i, j)
    return False


def solve():
    """
    Solve the problem by iterating over the matrix and finding active numbers.
    """
    gear_numbers = []
    result = 0

    for row in file_reader.read_input_file(__file__):
        matrix.append(list(row.strip()))

    possible_number = ""
    found_digits = False
    first_occurence = (0, 0)

    for i, row in enumerate(matrix):
        if found_digits:
            gear_check = is_gear_number(possible_number, first_occurence)
            if gear_check:
                gear_numbers.append({"number": int(possible_number), "coordinates": gear_check})

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
                gear_check = is_gear_number(possible_number, first_occurence)
                if gear_check:
                    gear_numbers.append({"number": int(possible_number), "coordinates": gear_check})
                found_digits = False
                possible_number = ""
                first_occurence = (0, 0)

    handled_gear_numbers = []
    # If the gear number's coordinates appear in the matrix more than twice, it is not a gear number
    for i, gear_number in enumerate(gear_numbers):
        if gear_number["coordinates"] not in handled_gear_numbers:
            matches = [gear_number]
            for other_gear_number in gear_numbers[i + 1:]:
                if gear_number["coordinates"] == other_gear_number["coordinates"]:
                    matches.append(other_gear_number)
            print(matches)
            if len(matches) == 2:
                result += matches[0]["number"] * matches[1]["number"]
            handled_gear_numbers.append(gear_number["coordinates"])
    
    print(result)
