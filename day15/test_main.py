from .main import part1, part2


INPUT = """
Disc #1 has 5 positions; at time=0, it is at position 4.
Disc #2 has 2 positions; at time=0, it is at position 1.
"""


def test_part1():
    assert part1(INPUT) == 5


def test_input():
    with open("input.txt") as file:
        input = file.read()

    assert part1(input) == 121834
    assert part2(input) == 3208099
