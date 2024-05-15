from .main import part1, part2


INPUT_1 = "ihgpwlah"
INPUT_2 = "kglvqrro"
INPUT_3 = "ulqzkmiv"


def test_part1():
    for input, expected in (
        (INPUT_1, "DDRRRD"),
        (INPUT_2, "DDUDRLRRUDRD"),
        (INPUT_3, "DRURDRUDDLLDLUURRDULRLDUUDDDRR")
    ):
        assert part1(input) == expected


def test_part2():
    for input, expected in (
        (INPUT_1, 370),
        (INPUT_2, 492),
        (INPUT_3, 830)
    ):
        assert part2(input) == expected


def test_input():
    input = "mmsxrhfx"

    assert part1(input) == "RLDUDRDDRR"
    assert part2(input) == 590
