from .main import part1, part2


INPUT = """"""


def test_part1():
    for input, expected in (
        ("R2, L3", 5),
        ("R2, R2, R2", 2),
        ("R5, L5, R5, R3", 12),
    ):
        assert part1(input) == expected


def test_part2():
    assert part2("R8, R4, R4, R8") == 4


def test_input():
    with open("input.txt") as file:
        input = file.read()

    assert part1(input) == 161
    assert part2(input) == 110
