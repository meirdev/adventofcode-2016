from .main import part1, part2


INPUT = """
rect 3x2
rotate column x=1 by 1
rotate row y=0 by 4
rotate column x=1 by 1
"""


def test_part1():
    assert part1(INPUT, (7, 3)) == 6


def test_part2():
    assert part2(INPUT, (7, 3)) == "\n.#..#.#\n#.#....\n.#....."


def test_input():
    with open("input.txt") as file:
        input = file.read()

    assert part1(input) == 115
    # EFEYKFRFIJ
    assert part2(input) == "\n####.####.####.#...##..#.####.###..####..###...##.\n#....#....#....#...##.#..#....#..#.#......#.....#.\n###..###..###...#.#.##...###..#..#.###....#.....#.\n#....#....#......#..#.#..#....###..#......#.....#.\n#....#....#......#..#.#..#....#.#..#......#..#..#.\n####.#....####...#..#..#.#....#..#.#.....###..##.."
