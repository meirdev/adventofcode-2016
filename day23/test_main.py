from .main import part1, part2


INPUT = """
cpy 2 a
tgl a
tgl a
tgl a
cpy 1 a
dec a
dec a
"""


def test_part1():
    assert part1(INPUT) == 3


def test_input():
    with open("input.txt") as file:
        input = file.read()

    assert part1(input) == 11200
    assert part2(input) == 479007760
