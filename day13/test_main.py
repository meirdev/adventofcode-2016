from .main import part1, part2


INPUT = "10"


def test_part1():
    assert part1(INPUT, (4, 7)) == 11


def test_input():
    input = "1358"

    assert part1(input) == 96
    assert part2(input) == 141
