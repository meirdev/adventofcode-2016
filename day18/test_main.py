from .main import part1, part2


def test_part1():
    for input, rows, expected in (
        ("..^^.", 3, 6),
        (".^^.^.^^^^", 10, 38),
    ):
        assert part1(input, rows) == expected


def test_input():
    with open("input.txt") as file:
        input = file.read()

    assert part1(input) == 1961
    assert part2(input) == 20000795
