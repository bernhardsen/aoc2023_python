def day10():
    print("=== Day 10: Pipe Maze ===")
    with open("input/day10.txt") as f:
        data = f.read().replace("\r\n", "\n")
    pipe_map = data.split("\n")
    (start_x, start_y) = find_starting_point(pipe_map)

    print("-- Part 1: --")
    (steps, visited_tiles) = count_steps_to_loop(start_x, start_y, pipe_map)
    print(f"It takes {steps} steps for the animal to get back.")
    print(f"Therefor the furthest away is {int(steps / 2)} steps.")
    print()
    print("-- Part 2: --")
    contained = count_contained_tiles(pipe_map, visited_tiles)
    print(f"There are {contained} tiles inside the loop.")


def find_starting_point(map):
    for (y, line) in enumerate(map):
        for (x, char) in enumerate(line):
            if char == "S":
                return x, y


def count_steps_to_loop(start_x, start_y, pipe_map):
    x = start_x
    y = start_y
    steps = 0
    from_x = x
    from_y = y
    tiles_in_loop = []
    while steps == 0 or x != start_x or y != start_y:
        on_tile = pipe_map[y][x]
        tiles_in_loop.append(f"{x}x{y}")
        match on_tile:
            case "|":
                if from_y < y:
                    y += 1
                    from_y += 1
                else:
                    y -= 1
                    from_y -= 1
            case "-":
                if from_x < x:
                    x += 1
                    from_x += 1
                else:
                    x -= 1
                    from_x -= 1
            case "L":
                if from_y < y:
                    x += 1
                    from_y += 1
                else:
                    y -= 1
                    from_x -= 1
            case "J":
                if from_y < y:
                    x -= 1
                    from_y += 1
                else:
                    y -= 1
                    from_x += 1
            case "7":
                if from_y > y:
                    x -= 1
                    from_y -= 1
                else:
                    y += 1
                    from_x += 1
            case "F":
                if from_y > y:
                    x += 1
                    from_y -= 1
                else:
                    y += 1
                    from_x -= 1
            case "S":
                if pipe_map[y + 1][x] == "|" or pipe_map[y + 1][x] == "J" or pipe_map[y + 1][x] == "L":
                    y += 1
                elif pipe_map[y][x + 1] == "-" or pipe_map[y][x + 1] == "J" or pipe_map[y][x + 1] == "7":
                    x += 1
                else:
                    y -= 1

        steps += 1
    return steps, tiles_in_loop


def count_contained_tiles(pipe_map, loop):
    contained = 0
    for (y, line) in enumerate(pipe_map):
        is_inside = False
        in_pipe = False
        last_corner = "|"

        for (x, tile) in enumerate(line):

            if f"{x}x{y}" in loop:
                if in_pipe:
                    if tile == "J":
                        if last_corner == "F":
                            is_inside = not is_inside
                        in_pipe = False
                    elif tile == "7":
                        if last_corner == "L":
                            is_inside = not is_inside
                        in_pipe = False
                elif tile == "|":
                    is_inside = not is_inside
                else:
                    in_pipe = True
                    last_corner = tile
            elif is_inside:
                contained += 1

    return contained

