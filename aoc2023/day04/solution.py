from aoc2023.util import get_input


def solve_part1(cards):
    result = 0
    for card in cards:
        game, numbers = card.split(":")
        my_numbers, winning_numbers = numbers.split("|")
        my_numbers = my_numbers.split()
        winning_numbers = winning_numbers.split()
        score = 0
        for number in my_numbers:
            if number in winning_numbers:
                if score == 0:
                    score = 1
                else:
                    score *= 2
        result += score
    return result


class Card:
    def __init__(self, card_number, my_numbers, winning_numbers):
        self.card_number = card_number
        self.my_numbers = my_numbers
        self.winning_numbers = winning_numbers
        self.score = 0
        self.count = 1
        for number in self.my_numbers:
            if number in winning_numbers:
                self.score += 1
    def __repr__(self):
        return f"<Card {self.card_number} |score: {self.score}|count: {self.count}>"


def solve_part2(cards):
    original_cards = []
    for card in cards:
        card_number, game_numbers = card.split(":")
        _, card_number = card_number.split()
        my_numbers, winning_numbers = game_numbers.split("|")
        my_numbers = my_numbers.split()
        winning_numbers = winning_numbers.split()
        _card = Card(int(card_number), my_numbers, winning_numbers)
        original_cards.append(_card)

    for card in original_cards:
        #print(f"- card {card.card_number}")
        for count in range(card.count):
            #print(f" - count {count}")
            for i in range(0, card.score):
                try:
                    #print(f"  - adding 1 to {card.card_number+i}")
                    original_cards[card.card_number+i].count += 1
                except IndexError:
                    pass
    tally = 0
    for card in original_cards:
        tally += card.count
    return tally


if __name__ == "__main__":  # pragma: no cover
    entries = get_input("aoc2023/day04/input")
    print(solve_part1(entries))
    print(solve_part2(entries))