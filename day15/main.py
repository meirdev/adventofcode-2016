import itertools
import re
from typing import NamedTuple


class Disc(NamedTuple):
    id: int
    positions: int
    time: int
    position: int


def parse_input(input: str) -> list[Disc]:
    return list(
        map(
            lambda i: Disc(*map(int, i)),
            re.findall(
                r"Disc #(\d+) has (\d+) positions; at time=(\d+), it is at position (\d+).",
                input,
            ),
        )
    )


def solution(input: str, disc: Disc | None = None) -> int:
    discs = parse_input(input)

    if disc:
        discs.append(disc)

    for start_time in itertools.count():
        for time, disc in enumerate(discs, 1):
            if (disc.position + time + start_time) % disc.positions != 0:
                break
        else:
            return start_time

    return -1


def part1(input: str) -> int:
    return solution(input)


def part2(input: str) -> int:
    return solution(input, Disc(id=7, positions=11, time=0, position=0))


def main() -> None:
    with open("input.txt") as file:
        input = file.read()

    print("Part 1:", part1(input))
    print("Part 2:", part2(input))


if __name__ == "__main__":
    main()
