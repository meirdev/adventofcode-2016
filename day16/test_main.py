from .main import part1, part2


def test_part1():
    assert part1("10000", 20) == "01100"


def test_input():
    input = "10001110011110000"

    assert part1(input) == "10010101010011101"
    assert part2(input) == "01100111101101111"
