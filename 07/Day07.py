from collections import Counter
import fileinput

PUZZLE = [line.strip() for line in fileinput.input()]
HANDS = []

def camel_cards(data):
    sum = 0
    for i, (_, bid) in enumerate(sorted(data, key = lambda x: (rank(x[0]), tie_break(x[0]))), start = 1):
        sum += bid * i
    return sum

def camel_cards_part_two(data):
    sum = 0
    for i, (_, bid) in enumerate(sorted(data, key = lambda x: (rank(x[0], True), tie_break(x[0], True))), start = 1):
        sum += bid * i
    return sum

def rank(hand, isPartTwo = False):

    if isPartTwo and hand != 'JJJJJ':
        no_jokers = Counter(c for c in hand if c != 'J').most_common()
        hand = hand.replace('J', no_jokers[0][0])

    cmn = Counter(hand).most_common()

    #Five of a kind
    if cmn[0][1] == 5:
        return 6
    
    #Four of a kind
    if cmn[0][1] == 4:
        return 5
    
    #Full house & Three of a kind
    if cmn[0][1] == 3:
        return 2 + cmn[1][1]
    
    #Two pair & One paie
    if cmn[0][1] == 2:
        return cmn[1][1]
    
    return 0


def tie_break(hand, isPartTwo = False):
    return tuple(card_score(c, isPartTwo) for c in hand)

def card_score(card, isPartTwo = False):
    if isPartTwo:
        return 'J23456789TQKA'.index(card)
    return '23456789TJQKA'.index(card)

def parse_input(data):
    for line in data:
        hand, bid = line.split()
        HANDS.append((hand, int(bid)))


parse_input(PUZZLE)
print(f"Solution for part 1 is: {camel_cards(HANDS)}")
print(f"Solution for part 2 is: {camel_cards_part_two(HANDS)}")