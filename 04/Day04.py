import fileinput
from collections import defaultdict

PUZZLE = [line.strip() for line in fileinput.input()]
COPIES = defaultdict(int)
TOTAL = 0

def scratchcards(data):
    sum = 0
    for line in data:
        count = -1
        card, numbers = line.split(": ")
        id = card.split()[1]
        winning, you = numbers.split(" | ")
        winning = [x.strip() for x in winning.split()]
        you = [x.strip() for x in you.split()]
        for num in winning:
            if num in you:
                count += 1
        if count >= 0:
            sum += 2**(count)
    return sum


def scratchcards_part_two(data):
    COPIES = defaultdict(int)
    TOTAL = 0
    for line in data:
        count = 0
        card, numbers = line.split(": ")
        id = int(card.split()[1])
        winning, you = numbers.split(" | ")
        winning = [x.strip() for x in winning.split()]
        you = [x.strip() for x in you.split()]
        for num in winning:
            if num in you:
                count += 1
        COPIES[id] += 1
        print("count", count, id)
        for i in range(1, count + 1):
            COPIES[id + i] += 1 * COPIES[id]
        print(COPIES)
    for values in COPIES.values():
        TOTAL += values
    return TOTAL


print(f"Total score is: {scratchcards(PUZZLE)}")
print(f"Total scrathcards is: {scratchcards_part_two(PUZZLE)}")
