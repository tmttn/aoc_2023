""" Part 1 of day 3 of Advent of Code 2020. """
from common import file_reader


class ScratchCard:
    """A scratch card.

    Attributes:
        winning_numbers (list): The winning numbers on the scratch card.
        player_numbers (list): The numbers the player has.
    """

    winning_numbers = []
    player_numbers = []

    def __init__(self, line):
        # Parse the line to a scratch card. The line is in the format:
        # "Card   1: 82 41 56 54 18 62 29 55 34 20 | 37 14 10 80 58 11 65 96 90  8 59 32 53 21 98 83 17  9 87 25 71 77 70 73 24"
        self.parse_line(line)

    def parse_line(self, line):
        """
        Parses a line of input and extracts the winning numbers and player numbers.

        Args:
            line (str): The input line to parse.

        Returns:
            None
        """

        # Split the line into the card number, the winning numbers, and the player numbers
        numbers = line.split(":")[1]

        self.winning_numbers = [
            int(number) for number in numbers.split("|")[0].strip().split()
        ]
        self.player_numbers = [
            int(number) for number in numbers.split("|")[1].strip().split()
        ]

    def calculate_points(self):
        """
        Calculates the points for the player based on the winning numbers.

        Returns:
            int: The total points earned by the player.
        """
        points = 0
        for number in self.player_numbers:
            # Check if the number is a winning number
            if number in self.winning_numbers:
                if points == 0:
                    points = 1
                else:
                    points *= 2
        return points


def solve():
    """
    Solves the problem by reading input from a file, parsing each line to a scratch card,
    and calculating the points for each card. The total points are then printed.
    """
    result = 0
    for line in file_reader.read_input_file(__file__):
        card = ScratchCard(line)
        result += card.calculate_points()

    print(result)
