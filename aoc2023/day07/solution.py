from aoc2023.util import get_input

from collections import Counter, defaultdict
from sortedcontainers import SortedList

CARD_VALUES = {
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "T": 10,
    "J": 11,
    "Q": 12,
    "K": 13,
    "A": 14,
}

HAND_VALUES = {
    "Five of a kind": 7,
    "Four of a kind": 6,
    "Full house": 5,
    "Three of a kind": 4,
    "Two pair": 3,
    "One pair": 2,
    "High card": 1,
}


class Hand:
    def __init__(self, hand, bid):
        self.hand = hand
        self.bid = int(bid)
        self.hand_type = self._set_hand_type()
        self.hand_value = self._set_hand_value()

    def _set_hand_type(self):
        c = Counter(self.hand)
        if len(c) == 1:
            return "Five of a kind"
        elif len(c) == 2:
            if c.most_common()[0][1] == 4:
                return "Four of a kind"
            elif c.most_common()[0][1] == 3:
                return "Full house"
            else:
                raise Exception("Not a four of a kind or full house... impossible?")
        elif len(c) == 3:
            if c.most_common()[0][1] == 3:
                return "Three of a kind"
            elif c.most_common()[0][1] == 2:
                return "Two pair"
            else:
                raise Exception("Not a three of a kind or two pair... impossible?")
        elif len(c) == 4:
            return "One pair"
        elif len(c) == 5:
            return "High card"
        else:
            raise Exception("Not sure how you got here!")

    def _set_hand_value(self):
        return HAND_VALUES[self.hand_type]

    def __eq__(self, other):
        #print(f"__eq__: {self}; {other}")
        if self.hand_value != other.hand_value:
            return False
        for idx, card in enumerate(self.hand):
            if card != other.hand[idx]:
                return False
        return True
    
    def __gt__(self, other):
        #print(f"__gt__: self:{self} ? other:{other}")
        if self.hand_value < other.hand_value:
            return False
        if self.hand_value > other.hand_value:
            return True
        if self.hand_value == other.hand_value:
            #print(f"__gt__: {self.hand}@{self.hand_value} == {other.hand}@{other.hand_value}")
            for idx, card in enumerate(self.hand):
                #print(f"{idx}: {card}@{CARD_VALUES[card]} ? {other.hand[idx]}@{CARD_VALUES[other.hand[idx]]}")
                if CARD_VALUES[card] > CARD_VALUES[other.hand[idx]]:
                    return True
                elif CARD_VALUES[card] < CARD_VALUES[other.hand[idx]]:
                    return False

    def __repr__(self):
        return f"<Hand: {self.hand}: {self.hand_type}: bid {self.bid}: value: {self.hand_value}>"


def parse(entries):
    hands = defaultdict(list)
    for plays in entries:
        hand, bid = plays.split()
        h = Hand(hand, bid)
        hands[h.hand_type].append(h)
    return hands


def solve_part1(entries):
    hands = parse(entries)
    hand_types = [
        "Five of a kind",
        "Four of a kind",
        "Full house",
        "Three of a kind",
        "Two pair",
        "One pair",
        "High card",
    ]
    sl = SortedList()
    for hand_type in hand_types:
        for hand in hands[hand_type]:
            sl.add(hand)

    tally = 0
    rank = 1
    for hand in sl:
        tally += hand.bid * rank
        rank += 1
    return tally


def solve_part2(entries):
    return


if __name__ == "__main__":  # pragma: no cover
    entries = get_input("aoc2023/day07/input")
    print(solve_part1(entries))
    print(solve_part2(entries))
