"""This module contains the solution for Part 2 of Day 2 of the Advent of Code 2023 challenge.

The module includes a function `solve()` that calculates the result by reading input from a file,
parsing the game data, and calculating the power of the minimal set of marbles that is required to
play the game.

The power of a set of marbles is equal to the numbers of
red, green, and blue marbles multiplied together.
"""
from common import file_reader
from .game_util import parse_game


def solve():
    """Solves the game and prints the result.

    This function reads the input file, parses the game data, and calculates the power of the
    minimal set of marbles that is required to play the game. Finally, it prints the result.
    """
    result = 0

    for line in file_reader.read_input_file(__file__):
        game = parse_game(line)

        # Calculate the power of the minimal set of marbles that is required to play the game
        red_marbles = 0
        green_marbles = 0
        blue_marbles = 0

        for draw in game.draws:
            for marble in draw:
                if marble.color == "red":
                    red_marbles = max(red_marbles, marble.number)
                elif marble.color == "green":
                    green_marbles = max(green_marbles, marble.number)
                elif marble.color == "blue":
                    blue_marbles = max(blue_marbles, marble.number)

        result += red_marbles * green_marbles * blue_marbles

    # Print the result
    print(result)
