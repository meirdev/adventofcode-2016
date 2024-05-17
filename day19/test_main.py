from .main import part1, part2


INPUT = 5


def test_part1():
    assert part1(INPUT) == 3


def test_part2():
    assert part2(INPUT) == 2


def test_input():
    input = 3005290

    assert part1(input) == 1816277
    assert part2(input) == 1410967
