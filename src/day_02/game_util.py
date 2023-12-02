"""
This module contains utility functions and classes for a game involving marbles.

Classes:
- Marble: Represents a marble from a bag of marbles.
- Round: Represents a round from a game.
- Game: Represents a game.

Functions:
- parseMarble: Parses a marble from a string to a Marble object.
- parseDraw: Parses a draw from a string to a list of Marble objects.
- parseDraws: Parses a list of rounds from a string to a list of Round objects.
- parseGame: Parses a game from a line of input to a Game object.
"""


class Marble:
    """A marble from a bag of marbles.

    Attributes:
        color (str): The color of the marble.
        number (int): The number of marbles drawn.
    """

    def __init__(self, color, number):
        self.color = color
        self.number = number


class Game:
    """A game.

    Attributes:
        number (int): The game number.
        draws (list): A list of draws.
    """

    def __init__(self):
        self.number = 0
        self.draws = []


def parse_marble(marble):
    """Parses a marble from a string to a Marble object.

    Args:
        marble (str): A string representing a marble.

    Returns:
        Marble: A Marble object representing the parsed marble.

    Example:
        >>> parseMarble("1 blue")
        Marble(color='blue', number=1)
    """
    marble = marble.strip().split(" ")
    return Marble(marble[1], int(marble[0]))


def parse_draw(draw):
    """Parses a draw from a string to a list of Marble objects.

    Args:
        draw (str): A string representing a draw.

    Returns:
        list: A list of Marble objects representing the parsed draw.

    Example:
        >>> parseDraw("1 blue, 4 green, 1 red")
        [Marble(color='blue', number=1), Marble(color='green', number=4), Marble(color='red', number=1)]
    """
    draw = draw.split(",")
    return [parse_marble(marble) for marble in draw]


def parse_draws(draws):
    """Parses a list of rounds from a string to a list of Round objects.

    Args:
        draws (str): A string representing a list of rounds.

    Returns:
        list: A list of Round objects representing the parsed list of rounds.

    Example:
        >>> parseDraws("1 blue, 4 green, 1 red; 5 green, 3 blue; 9 green, 4 blue; 3 blue, 1 red, 10 green; 6 green, 2 blue")
        [
            [Marble(color='blue', number=1), Marble(color='green', number=4), Marble(color='red', number=1)],
            [Marble(color='green', number=5), Marble(color='blue', number=3)],
            [Marble(color='green', number=9), Marble(color='blue', number=4)],
            [Marble(color='blue', number=3), Marble(color='red', number=1), Marble(color='green', number=10)],
            [Marble(color='green', number=6), Marble(color='blue', number=2)]
        ]
    """
    draws = draws.split(";")
    return [parse_draw(draw) for draw in draws]


def parse_game(line):
    """Parses a game from a line of input to a Game object.

    Args:
        line (str): A string representing a game.

    Returns:
        Game: A Game object representing the parsed game.

    Example:
        >>> parseGame("Game 9: 1 blue, 4 green, 1 red; 5 green, 3 blue; 9 green, 4 blue; 3 blue, 1 red, 10 green; 6 green, 2 blue")
        Game(number=9, draws=[
            [Marble(color='blue', number=1), Marble(color='green', number=4), Marble(color='red', number=1)],
            [Marble(color='green', number=5), Marble(color='blue', number=3)],
            [Marble(color='green', number=9), Marble(color='blue', number=4)],
            [Marble(color='blue', number=3), Marble(color='red', number=1), Marble(color='green', number=10)],
            [Marble(color='green', number=6), Marble(color='blue', number=2)]
        ])
    """
    game = Game()
    game_number, draws = line.split(":")
    game.number = int(game_number.split(" ")[1])
    game.draws = parse_draws(draws)
    return game
