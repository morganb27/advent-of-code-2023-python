from collections import Counter
import fileinput

PUZZLE = [line.strip() for line in fileinput.input()]
HANDS = []

def camel_cards(data):
    sum = 0
    for i, (hand, bid) in enumerate(sorted(data, key = lambda x: (rank(x[0]), tie_break(x[0]))), start = 1):
        
        print(i, hand, bid)
        sum += bid * i
    return sum

def rank(hand):
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


def tie_break(hand):
    return tuple(card_score(c) for c in hand)

def card_score(card):
    return '23456789TJQKA'.index(card)

def parse_input(data):
    for line in data:
        hand, bid = line.split()
        HANDS.append((hand, int(bid)))


parse_input(PUZZLE)
print(f"Solution for part 1 is: {camel_cards(HANDS)}")