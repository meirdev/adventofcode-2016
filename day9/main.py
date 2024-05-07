import re
from typing import Callable

RE = re.compile(r"\((\d+)x(\d+)\)")


def parse_input(input: str) -> str:
    return input.strip()


def decompress_length(
    compress: str, pos: int, end_pos: int, fn: Callable[[str, int, int], int]
) -> int:
    length = 0

    while pos < len(compress):
        result = RE.search(compress, pos, end_pos)
        if result:
            chars = int(result.group(1))
            repeat = int(result.group(2))

            start, end = result.span()

            length += (start - pos) + fn(compress, end, end + chars) * repeat
            pos = result.end() + chars
        else:
            length += end_pos - pos
            break

    return length


def solution(input: str, fn: Callable[[str, int, int], int]) -> int:
    compress = parse_input(input)

    return decompress_length(compress, 0, len(compress), fn)


def part1(input: str) -> int:
    return solution(input, lambda _, start, end: end - start)


def part2(input: str) -> int:
    def fn(data, start, end):
        return decompress_length(data, start, end, fn)

    return solution(input, fn)


def main() -> None:
    with open("input.txt") as file:
        input = file.read()

    print("Part 1:", part1(input))
    print("Part 2:", part2(input))


if __name__ == "__main__":
    main()
