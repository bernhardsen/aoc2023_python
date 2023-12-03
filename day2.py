from dataclasses import dataclass


def day2():
    print("=== Day 2: Cube Conundrum ===")
    with open("input/day2.txt") as f:
        data = f.read()
    games = parse_games(data)

    print("-- Part 1: --")
    sum_of_possible_ids = 0
    for game in games:
        is_possible = True
        for rnd in game.rounds:
            is_possible = is_possible and rnd.red <= 12 and rnd.green <= 13 and rnd.blue <= 14
        if is_possible:
            sum_of_possible_ids += game.id
    print(f"The sum of the IDs of the possible games is {sum_of_possible_ids}.")

    print("\n-- Part 2: --")
    total_power = sum(map(get_power_of_game, games))
    print(f"The sum of total power of the games is {total_power}.")


def get_power_of_game(game):
    red = max(map(lambda rnd: rnd.red, game.rounds))
    green = max(map(lambda rnd: rnd.green, game.rounds))
    blue = max(map(lambda rnd: rnd.blue, game.rounds))
    return red * green * blue


def parse_games(data):
    lines = data.split("\n")
    games = []
    for line in lines:
        parts = line.split(": ")
        id_parts = parts[0].split(" ")
        game_id = int(id_parts[1])
        rounds = parts[1].split(";")
        game_rounds = []
        for rnd in rounds:
            assignments = rnd.strip().split(", ")
            red = green = blue = 0
            for assignment in assignments:
                ass_parts = assignment.strip().split(" ")
                match ass_parts[1]:
                    case "red":
                        red = int(ass_parts[0])
                    case "green":
                        green = int(ass_parts[0])
                    case "blue":
                        blue = int(ass_parts[0])
            game_rounds.append(Round(red, green, blue))
        games.append(Game(game_id, game_rounds))
    return games


@dataclass
class Round:
    red: int
    green: int
    blue: int


@dataclass
class Game:
    id: int
    rounds: [Round]
