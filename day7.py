from dataclasses import dataclass


def day7():
    print("=== Day 7: Camel Cards ===")
    with open("input/day7.txt") as f:
        data = f.read().replace("\r\n", "\n")

    print("-- Part 1: --")
    hands1 = parse_input(data=data)
    score = score_hands(hands1)
    print(f"The total score of all the hands is {score}")

    print("\n-- Part 2: --")
    hands2 = parse_input(data=data.replace("J", "?"))
    score = score_hands(hands2)
    print(f"If we play with jokers, the total score is {score}")


def parse_input(data):
    hands = []
    for line in data.split("\n"):
        parts = line.split(" ")
        cards = []
        for c in parts[0]:
            cards.append(card_val(c))
        hands.append(CamelHand(cards, int(parts[1]), score_hand(cards)))
    return hands


def score_hands(hands):
    total = 0
    hands = list(sorted(hands, key=lambda h: (h.score, h.cards[0], h.cards[1], h.cards[2], h.cards[3], h.cards[4])))
    for i in range(1, len(hands) + 1):
        total += hands[i - 1].value * i
    return total


def card_val(card):
    match card:
        case '?':
            return 1
        case 'A':
            return 14
        case 'K':
            return 13
        case 'Q':
            return 12
        case 'J':
            return 11
        case 'T':
            return 10
        case _:
            return int(card)


def score_hand(cards):
    cards = list(filter(lambda card: card != 1, cards))
    jokers = 5 - len(cards)
    if jokers == 5:
        return 7
    cards.sort()
    counts = {}
    for i in range(14):
        counts[i + 1] = 0
    for i in range(len(cards)):
        counts[cards[i]] += 1

    ordered_counts = list(reversed(sorted(counts.values())))
    ordered_counts[0] += jokers
    if ordered_counts[0] == 5:
        return 7
    elif ordered_counts[0] == 4:
        return 6
    elif ordered_counts[0] == 3 and ordered_counts[1] == 2:
        return 5
    elif ordered_counts[0] == 3:
        return 4
    elif ordered_counts[0] == 2 and ordered_counts[1] == 2:
        return 3
    elif ordered_counts[0] == 2:
        return 2
    return 1


@dataclass
class CamelHand:
    cards: [int]
    value: int
    score: int
