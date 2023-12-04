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
        Parses a line of input and extracts the card number, winning numbers, and player numbers.

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

    def calculate_copies(self):
        """
        Calculate the number of scratch cards in line the player should receive a copy for.

        Returns:
            int: The number of scratch cards.
        """
        copies = 0
        for number in self.player_numbers:
            # Check if the number is a winning number
            if number in self.winning_numbers:
                copies += 1
        return copies


def solve():
    """
    Solves the problem by calculating the total number of scratch cards.
    """
    result = 0
    lines = file_reader.read_input_file(__file__)
    card_count = [1 for line in lines]
    for i, line in enumerate(lines):
        card = ScratchCard(line)
        copies = card.calculate_copies()
        for j in range(i + 1, i + copies + 1):
            if j < len(lines):
                card_count[j] += 1 * card_count[i]

    for count in card_count:
        result += count
    print(result)
