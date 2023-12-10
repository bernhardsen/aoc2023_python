from dataclasses import dataclass


def day8():
    print("=== Day 8: Haunted Wasteland ===")
    with open("input/day8.txt") as f:
        data = f.read().replace("\r\n", "\n")

    data_parts = data.split("\n\n")
    actions = data_parts[0]
    nodes = parse_nodes(data_parts[1])

    print("-- Part 1: --")
    (steps, _) = count_steps(nodes, actions, "AAA", "ZZZ")
    print(f"It takes {steps} steps to get from AAA to ZZZ")

    print()
    print("-- Part 2: --")
    starters = list(filter(lambda k: k.endswith("A"), nodes.keys()))
    initial_z = list(map(lambda starter: count_steps(nodes, actions, starter, "Z"), starters))
    back_to_z = list(map(lambda t: count_steps(nodes, actions, t[1], t[1]), initial_z))
    steps = sync_them_up(initial_z, back_to_z)
    print(f"It takes {steps} until everyone ends up on a node ending with Z.")


def sync_them_up(initial, back):
    step_size = back[0][0]
    position = step_size * initial[0][0]
    while True:
        all_synced = True
        for index, i in enumerate(initial):
            if (position - i[0]) % back[index][0] != 0:
                all_synced = False
        if all_synced:
            return position
        position += step_size


def parse_nodes(node_data):
    nodes = {}
    for line in node_data.split("\n"):
        node_id = line[0:3]
        nodes[node_id] = Node(node_id, line[7:10], line[12:15])
    return nodes


def count_steps(nodes, actions, start, end):
    steps = 0
    current = start
    while steps == 0 or not current.endswith(end):
        if actions[steps % len(actions)] == "L":
            current = nodes[current].left
        else:
            current = nodes[current].right
        steps += 1
    return steps, current


@dataclass
class Node:
    id: str
    left: str
    right: str
