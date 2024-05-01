from .main import part1, part2


INPUT_1 = """5 10 25"""

INPUT_2 = """
101 301 501
102 302 502
103 303 503
201 401 601
202 402 602
203 403 603
"""


def test_part1():
    assert part1(INPUT_1) == 0


def test_part2():
    assert part2(INPUT_2) == 6


def test_input():
    with open("input.txt") as file:
        input = file.read()

    assert part1(input) == 917
    assert part2(input) == 1649
