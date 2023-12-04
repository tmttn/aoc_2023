"""
This is the main script for the Advent of Code 2023 project.
It allows the user to run the solution for a specific day and part.
"""
import argparse
import importlib
import os
import sys

# Parse the command line arguments
parser = argparse.ArgumentParser(description="Advent of Code 2023")
parser.add_argument(
    "day",
    metavar="day",
    type=int,
    help="the day of the challenge (1-25)",
)
parser.add_argument(
    "part",
    metavar="part",
    type=int,
    help="the part of the challenge (1 or 2)",
)
parser.add_argument(
    "--input",
    metavar="input",
    type=str,
    help="the path to the input file",
)
args = parser.parse_args()

# Check if the input file exists
if args.input and not os.path.isfile(args.input):
    print(f"Input file {args.input} does not exist.")
    sys.exit(1)
    
# Import the module for the given day and part
module_name = f"day_{args.day:02d}.part_{args.part}"
try:
    module = importlib.import_module(module_name)
except ModuleNotFoundError:
    print(f"Module {module_name} not found.")
    sys.exit(1)
    
# Solve the puzzle
module.solve()
