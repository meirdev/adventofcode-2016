from .main import part1, part2


INPUT = """
ULL
RRDDD
LURDL
UUUUD
"""


def test_part1():
    assert part1(INPUT) == "1985"


def test_part2():
    assert part2(INPUT) == "5DB3"


def test_input():
    with open("input.txt") as file:
        input = file.read()

    assert part1(input) == "38961"
    assert part2(input) == "46C92"
