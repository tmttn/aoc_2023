from common import file_reader

# Remove all non-digit characters from the line and
# return the concatenation of the first and last digits as an integer
#
# Example: '895foureightckjjl1' -> 81
def getCalibrationValue(line):
    return int(''.join(filter(str.isdigit, line))[0] + ''.join(filter(str.isdigit, line))[-1])

def solve():
    result = 0

    # Iterate through each line and add the calibration value to the result
    for line in file_reader.read_input_file(__file__):
        result += getCalibrationValue(line)

    # Print the result
    print(result)
