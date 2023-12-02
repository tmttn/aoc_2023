"""_summary_

    Returns:
        _type_: _description_
    """
import os


def read_input_file(file):
    """
    Reads the contents of the input file.

    Args:
        file (str): The path to the input file.

    Returns:
        str: The contents of the input file as a string.
    """
    # Change the working directory
    os.chdir(os.path.dirname(os.path.abspath(file)))

    # Read the input file
    with open("input.txt", "r", encoding="utf-8") as file:
        return file.readlines()
