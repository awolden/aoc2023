
from aoc2023.utils import loader
import re

mapping = {
        'zero': '0',
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9',
    }


def process():
    inputs = loader.load_day('day1')
    print(sum_calibration_values(inputs))
    print(sum_calibration_values_part_2(inputs))

def sum_calibration_values_part_2(lines):
    sum = 0
    for line in lines:
        pattern = re.compile(r'(?=(one|two|three|four|five|six|seven|eight|nine|\d))')
        found = pattern.findall(line)
        found = [mapping.get(word, word) for word in found]

        first_digit, last_digit = found[0], found[-1]
        sum += int(first_digit + last_digit)

    return sum


def sum_calibration_values(lines):
    total_sum = 0
    for line in lines:
        first_digit = next(char for char in line if char.isdigit())
        last_digit = next(char for char in reversed(line) if char.isdigit())
        calibration_value = int(first_digit + last_digit)
        total_sum += calibration_value
    
    return total_sum
if __name__ == "__main__":
    process()

