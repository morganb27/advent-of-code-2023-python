import fileinput
from collections import defaultdict
import operator
from functools import reduce

PUZZLE = [line.strip() for line in fileinput.input()]
SYMBOLS = defaultdict(str)
PARTS = []
VALID = "/*@-+=$#&%"
SEEN = set()
RATIO = 0

def part_numbers(data):
    global RATIO
    sum = 0
    for x, line in enumerate(data):
        num = ''
        start = None
        for y, c in enumerate(line):
            if (c == '.' or c in VALID) and num:
                PARTS.append([int(num), x, start, y - 1])
                num = ''
                start = None
                if c in VALID:
                    SYMBOLS[x, y] = c
            elif c in VALID:
                if num:
                    num = ''
                SYMBOLS[x, y] = c
            elif c.isdigit():
                if start is None:
                    start = y
                num += c
                if y == len(line) - 1:
                    PARTS.append([int(num), x, start, y - 1])
    for x, y in SYMBOLS:
        for val, row, start, end in PARTS:
            if (start - 1 <= y <= end + 1) and (row - 1 <= x <= row + 1):
                if f"{row},{start},{end}" not in SEEN:
                    sum += val
                SEEN.add(f"{row},{start},{end}")
    return sum

def gear_ratio():
    sum = 0
    for (x, y), s in SYMBOLS.items():
        if s == "*":
            nums = []
            for val, row, start, end in PARTS:
                if (start - 1 <= y <= end + 1) and (row - 1 <= x <= row + 1):
                    nums.append(val)
            if len(nums) == 2:
                sum += reduce(operator.mul, nums, 1)
    return sum


print(f"Sum of all part numbers is: {part_numbers(PUZZLE)}")
print(f"Sum of all gear ratio is: {gear_ratio()}")