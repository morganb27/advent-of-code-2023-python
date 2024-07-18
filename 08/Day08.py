import fileinput
from collections import defaultdict

PUZZLE = [line.strip() for line in fileinput.input()]
INSTRUCTIONS = PUZZLE[0]
NETWORK = defaultdict(tuple)

def haunted_wasteland():
    node = 'AAA'
    i = 0
    while node != 'ZZZ':
        instruction = INSTRUCTIONS[i % len(INSTRUCTIONS)]
        child = 0 if instruction == 'L' else 1
        node = NETWORK[node][child]
        i += 1
    return i
    

def haunted_wasteland_part_two():
    start = [node for node in NETWORK if node.endswith('A')]
    i = 0
    print(start)
    while not any(node.endswith('Z') for node in start) and i < 10000000:
        instruction = INSTRUCTIONS[i % len(INSTRUCTIONS)]
        child = 0 if instruction == 'L' else 1
        for j, n in enumerate(start):
            start[j] = NETWORK[n][child]
        i += 1
        print(start)
    return i

def parse_input(data):
    for line in data[2:]:
        node, children = line.split(' = ')
        left, right = children.strip('(').strip(')').split(', ')
        NETWORK[node] = (left, right)

parse_input(PUZZLE)
print(f"Solution for part 1 is: {haunted_wasteland()}")
print(f"Solution for part 2 is: {haunted_wasteland_part_two()}")