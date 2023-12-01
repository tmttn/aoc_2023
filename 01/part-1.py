import os

# Change the working directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Read the input file
with open('input.txt', 'r') as file:
    lines = file.readlines()

sum = 0

# Remove all non-digit characters from the line and return the concatenation of the first and last digits as an integer
# Example: '895foureightckjjl1' -> 81
def getCalibrationValue(line):
    return int(''.join(filter(str.isdigit, line))[0] + ''.join(filter(str.isdigit, line))[-1])
    

# Iterate through each line and add the calibration value to the sum
for line in lines:
    sum += getCalibrationValue(line)

# Print the sum
print(sum)