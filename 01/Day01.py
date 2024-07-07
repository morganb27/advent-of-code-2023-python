import fileinput

PUZZLE = [line.strip() for line in fileinput.input()]
D = {
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9
    }

def calibration_values(data):
    sum = 0
    for line in data:
        sum += parse_input(line)
    return sum

def calibration_values_part_two(data):
    sum = 0
    for line in data:
        sum += parse_input_part_two(line)
    return sum

def parse_input(line):
    a = None
    for c in line:
        if c.isdigit():
            if a is None:
                a = int(c)
            b = int(c)
    return a * 10 + b

def parse_input_part_two(line):
    a = None
    for i, c in enumerate(line):
        if c.isdigit():
            if a is None:
                a = int(c)
            b = int(c)
        elif line[i:i+3] in D:
            if a is None:
                a = D[line[i:i+3]]
            b = D[line[i:i+3]]
        elif line[i:i+4] in D:
            if a is None:
                a = D[line[i:i+4]]
            b = D[line[i:i+4]]
        elif line[i:i+5] in D:
            if a is None:
                a = D[line[i:i+5]]
            b = D[line[i:i+5]]
    return a * 10 + b

print(f"Solution for part 1 is: {calibration_values(PUZZLE)}")
print(f"Solution for part 2 is: {calibration_values_part_two(PUZZLE)}")