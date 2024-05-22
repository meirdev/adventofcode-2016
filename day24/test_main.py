from .main import part1, part2


INPUT = """
###########
#0.1.....2#
#.#######.#
#4.......3#
###########
"""


def test_part1():
    assert part1(INPUT) == 14


def test_input():
    with open("input.txt") as file:
        input = file.read()

    assert part1(input) == 412
    assert part2(input) == 664
