# Advent of Code 2023!
import sys

from day1 import day1
from day2 import day2

print('Advent of Code 2023!')
if len(sys.argv) == 2:
    match sys.argv[1]:
        case "1":
            day1()
        case "2":
            day2()
        case _:
            print(f"Day {sys.argv[1]} not implemented yet")
else:
    print('The first and only argument should be which day to run.')


