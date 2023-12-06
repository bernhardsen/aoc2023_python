from dataclasses import dataclass
from math import sqrt, ceil


def day6():
    print("=== Day 6: Wait For It ===")
    with open("input/day6.txt") as f:
        data = f.read().replace("\r\n", "\n")

    print("-- Part 1: --")
    total = calculate_race_leniency(parse_input_multiple(data))
    print(f"When we multiply all together we get {total} ways.")

    print("\n-- Part 2: --")
    total = calculate_race_leniency(parse_input_single(data))
    print(f"If its just one race, we get {total} ways.")


def parse_input_multiple(data):
    races = []
    lines = data.split("\n")
    num_races = int((len(lines[0]) - 8) / 7)
    for i in range(num_races):
        s_start = 9 + i * 7
        races.append(Race(
            int(lines[0][s_start:s_start + 7].strip()),
            int(lines[1][s_start:s_start + 7].strip())
        ))
    return races


def parse_input_single(data):
    lines = data.split("\n")
    return [Race(
        int(lines[0][9::].replace(" ", "")),
        int(lines[1][9::].replace(" ", ""))
    )]


def calculate_race_leniency(races):
    total = 1
    for r in range(len(races)):
        short = ceil((races[r].time - sqrt(races[r].time * races[r].time - ((races[r].distance + 1) * 4.0))) / 2.0)
        long = races[r].time - short
        total *= long - short + 1
    return total


@dataclass
class Race:
    time: int
    distance: int
