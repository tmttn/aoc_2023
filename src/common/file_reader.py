"""This module contains the function for reading the input file for the given module.
"""
import os

def read_input_file(file):
    """Reads the input file for the given module.
    
    Parameters:
    file (str): The path to the module.
    
    Returns:
    list: A list of strings representing the lines from the input file.
    """
    # Change the working directory
    os.chdir(os.path.dirname(os.path.abspath(file)))

    # Read the input file
    with open("input.txt", "r", encoding="utf-8") as file:
        return file.readlines()
