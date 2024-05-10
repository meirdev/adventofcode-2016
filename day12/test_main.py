from .main import part1, part2


INPUT = """
cpy 41 a
inc a
inc a
dec a
jnz a 2
dec a
"""


def test_part1():
    assert part1(INPUT) == 42


def test_input():
    with open("input.txt") as file:
        input = file.read()

    assert part1(input) == 318003
    assert part2(input) == 9227657
