from .main import part1, part2


INPUT = "abc"


def test_part1():
    assert part1(INPUT) == "18f47a30"


def test_part2():
    assert part2(INPUT) == "05ace8e3"


def test_input():
    input = "abbhdwsy"

    assert part1(input) == "801b56a7"
    assert part2(input) == "424a0197"
