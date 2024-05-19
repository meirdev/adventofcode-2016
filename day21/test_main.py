from .main import part1, part2


INPUT = """
swap position 4 with position 0
swap letter d with letter b
reverse positions 0 through 4
rotate left 1 step
move position 1 to position 4
move position 3 to position 0
rotate based on position of letter b
rotate based on position of letter d
"""


def test_part1():
    assert part1(INPUT, "abcde") == "decab"


def test_part2():
    assert part2(INPUT, "decab") == "abcde"


def test_input():
    with open("input.txt") as file:
        input = file.read()

    assert part1(input) == "dgfaehcb"
    assert part2(input) == "fdhgacbe"
