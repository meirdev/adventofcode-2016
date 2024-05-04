from .main import part1, part2


INPUT = """
eedadn
drvtee
eandsr
raavrd
atevrs
tsrnev
sdttsa
rasrtv
nssdts
ntnada
svetve
tesnvt
vntsnd
vrdear
dvrsen
enarar
"""


def test_part1():
    assert part1(INPUT) == "easter"


def test_part2():
    assert part2(INPUT) == "advent"


def test_input():
    with open("input.txt") as file:
        input = file.read()

    assert part1(input) == "xdkzukcf"
    assert part2(input) == "cevsgyvd"
