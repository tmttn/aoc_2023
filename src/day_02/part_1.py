"""This module contains the solution for Part 1 of Day 2 of the Advent of Code 2023 challenge.

The module includes a function `solve()` that calculates the result by reading input from a file,
parsing the game data, and checking if the draws are possible for a given set of marbles.
The result is then printed to the console.
"""
from common import file_reader
from .game_util import parseGame

def solve():
    """Solves the game and prints the result.

    This function reads the input file, parses the game data, and checks if the draws are possible
    for a bag with a specific number of red, green, and blue marbles. It then calculates the result
    by summing the numbers of the possible games. Finally, it prints the result.
    """
    result = 0

    for line in file_reader.read_input_file(__file__):
        game = parseGame(line)
        
        game_possible = True

        # Check if the game's draws are possible for a bag
        # with 12 red marbles, 13 green marbles, and 14 blue marbles
        for draw in game.draws:
            red_marbles = 0
            green_marbles = 0
            blue_marbles = 0

            for marble in draw:
                if marble.color == 'red':
                    red_marbles += marble.number
                elif marble.color == 'green':
                    green_marbles += marble.number
                elif marble.color == 'blue':
                    blue_marbles += marble.number

            if red_marbles > 12 or green_marbles > 13 or blue_marbles > 14:
                game_possible = False
                break

        if game_possible:
            result += game.number

    # Print the result
    print(result)
