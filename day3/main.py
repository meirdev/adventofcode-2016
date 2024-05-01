import itertools
import re
from typing import TypeAlias

Triangle: TypeAlias = tuple[int, int, int]


def is_valid_triangle(triangle: Triangle) -> bool:
    a, b, c = triangle

    return a + b > c and a + c > b and b + c > a


def parse_input(input: str) -> list[tuple[int, int, int]]:
    return [
        (int(a), int(b), int(c))
        for a, b, c in re.findall(r"(\d+)\s+(\d+)\s+(\d+)", input)
    ]


def part1(input: str) -> int:
    list_ = parse_input(input)

    return sum(1 for i in list_ if is_valid_triangle(i))


def part2(input: str) -> int:
    list_ = parse_input(input)

    return sum(
        1
        for i in itertools.batched(itertools.chain.from_iterable(zip(*list_)), 3)
        if is_valid_triangle(i)
    )


def main() -> None:
    with open("input.txt") as file:
        input = file.read()

    print("Part 1:", part1(input))
    print("Part 2:", part2(input))


if __name__ == "__main__":
    main()
