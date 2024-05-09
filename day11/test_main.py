from .main import part1, part2


INPUT = """
The first floor contains a hydrogen-compatible microchip and a lithium-compatible microchip.
The second floor contains a hydrogen generator.
The third floor contains a lithium generator.
The fourth floor contains nothing relevant.
"""


def test_part1():
    assert part1(INPUT) == 11


def test_input():
    with open("input.txt") as file:
        input = file.read()

    assert part1(input) == 31
    assert part2(input) == 55
