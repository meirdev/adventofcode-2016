from typing import Iterator

import ranges

MAX_VALUE = 2**32


def parse_input(input: str) -> ranges.RangeSet:
    ip_addresses = ranges.RangeSet()

    for i in input.strip().splitlines():
        start, end = i.split("-")
        ip_addresses.add(ranges.Range(int(start), int(end), include_end=True))

    return ip_addresses


def solution(input: str, max_value: int) -> Iterator[int]:
    ip_addresses = parse_input(input)

    for i in ranges.RangeSet(ranges.Range(0, max_value)) - ip_addresses:
        start = i.start if i.include_start else i.start + 1
        end = i.end + 1 if i.include_end else i.end

        yield from range(start, end)


def part1(input: str, max_value: int = MAX_VALUE) -> int:
    return next(solution(input, max_value))


def part2(input: str, max_value: int = MAX_VALUE) -> int:
    return sum(1 for _ in solution(input, max_value))


def main() -> None:
    with open("input.txt") as file:
        input = file.read()

    print("Part 1:", part1(input))
    print("Part 2:", part2(input))


if __name__ == "__main__":
    main()
