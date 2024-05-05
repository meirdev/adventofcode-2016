from .main import IPv7, part1, part2


def test_part1():
    for input, expected in (
        ("abba[mnop]qrst", True),
        ("abcd[bddb]xyyx", False),
        ("aaaa[qwer]tyui", False),
        ("ioxxoj[asdfgh]zxcvbn", True),
    ):
        assert IPv7(input).is_support_tls() is expected


def test_part2():
    for input, expected in (
        ("aba[bab]xyz", True),
        ("xyx[xyx]xyx", False),
        ("aaa[kek]eke", True),
        ("zazbz[bzb]cdb", True),
    ):
        assert IPv7(input).is_support_ssl() is expected


def test_input():
    with open("input.txt") as file:
        input = file.read()

    assert part1(input) == 118
    assert part2(input) == 260
