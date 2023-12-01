import os
import re

# Change the working directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Read the input file
with open('input.txt', 'r') as file:
    lines = file.readlines()

sum = 0

def getCalibrationValue(input_string):
    pattern = re.compile(r'(?=(one|two|three|four|five|six|seven|eight|nine|\d))', re.IGNORECASE)
    matches = pattern.findall(input_string)

    if not matches:
        return None

    # Convert the first and last matches to integers
    first_match = int(matches[0]) if matches[0].isdigit() else int({'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}[matches[0].lower()])
    last_match = int(matches[-1]) if matches[-1].isdigit() else int({'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}[matches[-1].lower()])

    # Concatenate the first and last matches and return the result
    concatenated_result = int(f'{first_match}{last_match}')

    print(f'{input_string}: {first_match} + {last_match} = {concatenated_result}')
    return concatenated_result

# Iterate through each line and add the calibration value to the sum
for line in lines:
    sum += getCalibrationValue(line)

# Print the sum
print(sum)