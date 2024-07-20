import fileinput
from itertools import combinations

PUZZLE = [line.strip() for line in fileinput.input()]
GALAXIES = set()
EMPTY_ROWS = set(range(len(PUZZLE)))
EMPTY_COLS = set(range(len(PUZZLE[0])))
PART_1 = 0
PART_2 = 0


def cosmic_expansion():
    global PART_1, PART_2
    for (gx1, gy1), (gx2, gy2) in combinations(GALAXIES, 2):
        expansion = 0
        for i in range(min(gx1, gx2), max(gx1, gx2) + 1):
            if i in EMPTY_ROWS:
                expansion += 1
        
        for j in range(min(gy1, gy2), max(gy1, gy2) + 1):
            if j in EMPTY_COLS:
                expansion += 1
        
        manhattan_distance = abs(gx1 - gx2) + abs(gy1 - gy2)
        print("distance", manhattan_distance + expansion)
        PART_1 += manhattan_distance + expansion
        PART_2 += manhattan_distance + expansion * 999999

def find_galaxies(data):
    global GALAXIES
    for x, line in enumerate(data):
        for y, char in enumerate(line):
            if char == '#':
                GALAXIES.add((x, y))

def find_empty_rows_and_cols():
    global GALAXIES, EMPTY_ROWS, EMPTY_ROWS
    for (x, y) in GALAXIES:
        EMPTY_ROWS.discard(x)
        EMPTY_COLS.discard(y)





find_galaxies(PUZZLE)
find_empty_rows_and_cols()
cosmic_expansion()
print(GALAXIES)
print(EMPTY_ROWS)
print(EMPTY_COLS)
print(f"Solution for part 1 is: {PART_1}")
print(f"Solution to part 2 is: {PART_2}")
