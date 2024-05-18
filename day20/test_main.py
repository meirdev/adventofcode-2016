from .main import part1, part2


INPUT = """
5-8
0-2
4-7
"""


def test_part1():
    assert part1(INPUT, 10) == 3


def test_part2():
    assert part2(INPUT, 10) == 2


def test_input():
    with open("input.txt") as file:
        input = file.read()

    assert part1(input) == 23923783
    assert part2(input) == 125
