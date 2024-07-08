import fileinput
from collections import defaultdict

PUZZLE = [line.strip() for line in fileinput.input()]
CONSTRAINTS = {
    "red": 12,
    "green": 13,
    "blue": 14
}

def cube_conundrum(data):
    sum = 0
    for i, line in enumerate(data):
        if is_game_valid(line):
            sum += i + 1
    return sum

def cube_conundrum_part_two(data):
    sum = 0
    for line in data:
        sum += power(line)
    return sum


def is_game_valid(line):
    _, cubes = line.split(': ')
    for round in cubes.split('; '):
        for cube in round.split(', '):
            val, color = cube.split(' ')
            if int(val) > CONSTRAINTS[color]:
                return False
    return True

def power(line):
    d = defaultdict(int)
    result = 1
    _, cubes = line.split(': ')
    for round in cubes.split('; '):
        for cube in round.split(', '):
            val, color = cube.split(' ')
            if color not in d:
                d[color] = int(val)
            else:
                d[color] = max(d[color], int(val))
    for value in d.values():
        result *= value
    return result
        
print(f"Solution for part 1 is: {cube_conundrum(PUZZLE)}")
print(f"Solution for part 2 is {cube_conundrum_part_two(PUZZLE)}")

