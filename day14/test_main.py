from .main import part1, part2


INPUT = "abc"


def test_part1():
    assert part1(INPUT) == 22728


def test_part2():
    assert part2(INPUT) == 22551


def test_input():
    with open("input.txt") as file:
        input = file.read()

    assert part1(input) == 15035
    assert part2(input) == 19968
