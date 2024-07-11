import fileinput

PUZZLE = [line.strip() for line in fileinput.input()]
TIME = [int(x) for x in PUZZLE[0].split(":")[1].split()]
DISTANCE = [int(x) for x in PUZZLE[1].split(":")[1].split()]
print(TIME)
print(DISTANCE)

def boat_race():
    total = 1
    for t, d in zip(TIME, DISTANCE):
        sum = 0
        for x in range(t+1):
            if x * (t - x) > d:
                sum += 1
        total *= sum
    return total
        

print(f"Solution for part 1/part 2 is: {boat_race()}")