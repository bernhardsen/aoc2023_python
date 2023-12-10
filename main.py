# Advent of Code 2023!
import sys

from day1 import day1
from day10 import day10
from day2 import day2
from day3 import day3
from day4 import day4
from day5 import day5
from day6 import day6
from day7 import day7
from day8 import day8
from day9 import day9

print('Advent of Code 2023!')
if len(sys.argv) == 2:
    match sys.argv[1]:
        case "1":
            day1()
        case "2":
            day2()
        case "3":
            day3()
        case "4":
            day4()
        case "5":
            day5()
        case "6":
            day6()
        case "7":
            day7()
        case "8":
            day8()
        case "9":
            day9()
        case "10":
            day10()
        case _:
            print(f"Day {sys.argv[1]} not implemented yet")
else:
    print('The first and only argument should be which day to run.')


