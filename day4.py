

def day4():
    print("=== Day 4: Scratchcards ===")
    with open("input/day4.txt") as f:
        data = f.read()

    winners = []
    picks = []
    for line in data.split("\n"):
        parts = line.replace("  ", " ").split(": ")[1].split(" | ")
        winners.append(list(map(int, parts[1].split(" "))))
        picks.append(list(map(int, parts[0].split(" "))))

    print("-- Part 1: --")
    points = 0
    for i in range(0, len(picks)):
        points += calculate_score(len(list(filter(lambda pick: winners[i].count(pick) > 0, picks[i]))))
    print(f"We get a total of {points} points for all the tickets.")

    print("\n-- Part 2: --")
    held_tickets = [1] * len(picks)
    for i in range(0, len(picks)):
        correct_picks = len(list(filter(lambda pick: winners[i].count(pick) > 0, picks[i])))
        for j in range(i + 1, i + correct_picks + 1):
            held_tickets[j] += held_tickets[i]
    total_tickets = sum(held_tickets)
    print(f"We end up with a total of {total_tickets} tickets.")


def calculate_score(num):
    if num == 0:
        return 0
    return 1 << num - 1

