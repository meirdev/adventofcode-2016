from .main import part1, part2


INPUT = """
value 5 goes to bot 2
bot 2 gives low to bot 1 and high to bot 0
value 3 goes to bot 1
bot 1 gives low to output 1 and high to bot 0
bot 0 gives low to output 2 and high to output 0
value 2 goes to bot 2
"""


def test_part1():
    assert part1(INPUT, 2, 5) == 2


def test_input():
    with open("input.txt") as file:
        input = file.read()

    assert part1(input) == 113
    assert part2(input) == 12803
