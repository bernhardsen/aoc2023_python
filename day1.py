import re


def day1():
    print("=== Day 1: Trebuchet?! ===")
    with open("input/day1.txt") as f:
        data = f.read()

    calibration = calc_calibration(data)
    print("-- Part 1: --")
    print(f"The sum of all calibrations is {calibration}")

    cal2 = calc_calibration(data.replace("one", "o1e")
                            .replace("two", "t2o")
                            .replace("three", "t3e")
                            .replace("four", "f4r")
                            .replace("five", "f5e")
                            .replace("six", "s6x")
                            .replace("seven", "s7n")
                            .replace("eight", "e8t")
                            .replace("nine", "n9e"))
    print("\n-- Part 2: --")
    print(f"When we include numbers written as words, the sum is {cal2}!")


def calc_calibration(data):
    lines = data.split("\n")
    parts = map(first_and_last_digits, lines)
    return sum(parts)


def first_and_last_digits(s):
    return int(first_digit(s) + first_digit(s[::-1]))


def first_digit(s):
    match = re.search(r"\d", s)
    if match:
        return match.group()
    else:
        print("Not found!")
        return ""
