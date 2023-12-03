
def day3():
    print("=== Day 3: Gear Ratios ===")
    with open("input/day3.txt") as f:
        data = f.read()

    schematic = data.split("\n")  # x and y is reversed
    print("-- Part 1: --")

    width = len(schematic[0])
    height = len(schematic)

    touching_total = total_ratio = y = 0
    while y < height:
        x = 0
        while x < width:
            if is_numeric(x, y, schematic):
                num_width = 1
                while is_numeric(x + num_width, y, schematic):
                    num_width += 1

                if touches_symbols(x, y, num_width, schematic):
                    touching_total += int(schematic[y][x:x+num_width])
                x += num_width - 1
            x += 1
        y += 1

    print(f"The sum of the parts touching symbols is {touching_total}.")
    print("\n-- Part 2: --")

    y = 0
    while y < height:
        x = 0
        while x < width:
            if is_symbol(x, y, schematic):
                touching_numbers = []
                check_and_add_number(x - 1, y - 1, schematic, touching_numbers)
                check_and_add_number(x - 1, y, schematic, touching_numbers)
                check_and_add_number(x - 1, y + 1, schematic, touching_numbers)

                check_and_add_number(x, y - 1, schematic, touching_numbers)
                check_and_add_number(x, y + 1, schematic, touching_numbers)

                check_and_add_number(x + 1, y - 1, schematic, touching_numbers)
                check_and_add_number(x + 1, y, schematic, touching_numbers)
                check_and_add_number(x + 1, y + 1, schematic, touching_numbers)

                if len(touching_numbers) == 2:
                    total_ratio += touching_numbers[0] * touching_numbers[1]
            x += 1
        y += 1

    print(f"The sum of all the gear ratios is {total_ratio}.")


def check_and_add_number(x, y, schematic, numbers):
    n = get_number_at(x, y, schematic)
    if n != 0 and n not in numbers:
        numbers.append(n)


def get_number_at(x, y, schematic):
    if not is_numeric(x, y, schematic):
        return 0
    start = x
    while is_numeric(start - 1, y, schematic):
        start -= 1
    end = x
    while is_numeric(end + 1, y, schematic):
        end += 1
    return int(schematic[y][start:end + 1])


def touches_symbols(x, y, width, schematic):
    if (is_symbol(x - 1, y - 1, schematic) or is_symbol(x - 1, y, schematic) or is_symbol(x - 1, y + 1, schematic) \
            or is_symbol(x + width, y - 1, schematic) or is_symbol(x + width, y, schematic)
            or is_symbol(x + width, y + 1, schematic)):
        return True
    for i in range(width):
        if is_symbol(x + i, y - 1, schematic) or is_symbol(x + i, y + 1, schematic):
            return True
    return False


def is_numeric(x, y, schematic):
    return y < len(schematic) and x < len(schematic[0]) and '0' <= schematic[y][x] <= '9'


def is_symbol(x, y, schematic):
    return y < len(schematic) and x < len(schematic[0]) and schematic[y][x] != '.' and not is_numeric(x, y, schematic)


