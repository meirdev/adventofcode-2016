from .main import part1, part2


INPUT = """
aaaaa-bbb-z-y-x-123[abxyz]
a-b-c-d-e-f-g-h-987[abcde]
not-a-real-room-404[oarel]
totally-real-room-200[decoy]
"""


def test_part1():
    assert part1(INPUT) == 1514


def test_input():
    with open("input.txt") as file:
        input = file.read()

    assert part1(input) == 409147
    assert part2(input) == 991
