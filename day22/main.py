import itertools
import re
from typing import NamedTuple


class Node(NamedTuple):
    x: int
    y: int
    size: int
    used: int
    avail: int


def parse_input(input: str) -> list[Node]:
    return [
        Node(*map(int, i))
        for i in re.findall(
            r"/dev/grid/node-x(\d+)-y(\d+)\s+(\d+)T\s+(\d+)T\s+(\d+)T\s+(?:\d+)%", input
        )
    ]


def part1(input: str) -> int:
    nodes = parse_input(input)

    return sum(
        int(a.used != 0 and a.used <= b.avail) + int(b.used != 0 and b.used <= a.avail)
        for a, b in itertools.combinations(nodes, 2)
    )


def part2(input: str) -> int:
    nodes = parse_input(input)

    empty = next(node for node in nodes if node.used == 0)
    goal = max((node for node in nodes if node.y == 0), key=lambda node: node.x)

    board = {(node.y, node.x): node for node in nodes}


def main() -> None:
    with open("input.txt") as file:
        input = file.read()

    print("Part 1:", part1(input))
    print("Part 2:", part2(input))


if __name__ == "__main__":
    main()
