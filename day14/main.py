import functools
import hashlib
from typing import Callable, cast

import more_itertools


def find_first_triple(md5_hash: str) -> tuple[str, ...] | None:
    return next(
        (
            cast(tuple[str, ...], i)
            for i in more_itertools.windowed(md5_hash, 3)
            if more_itertools.all_equal(i)
        ),
        None,
    )


def in_five_times(md5_hash: str, char: str) -> bool:
    return char * 5 in md5_hash


@functools.cache
def generate_md5(s: str) -> str:
    md5 = hashlib.md5()
    md5.update(s.encode())
    return md5.hexdigest()


@functools.cache
def generate_md5_with_key_stretching(s: str, r: int = 2016) -> str:
    md5 = generate_md5(s)

    for _ in range(r):
        md5 = generate_md5(md5)

    return md5


def solution(input: str, fn: Callable[[str], str]) -> int:
    keys: list[int] = []

    i = 0

    while len(keys) < 64:
        if match := find_first_triple(fn(f"{input}{i}")):
            if any(
                in_five_times(fn(f"{input}{j}"), match[0])
                for j in range(i + 1, i + 1001)
            ):
                keys.append(i)

        i += 1

    return keys[-1]


def part1(input: str) -> int:
    return solution(input, generate_md5)


def part2(input: str) -> int:
    return solution(input, lambda s: generate_md5_with_key_stretching(s))


def main() -> None:
    input = "ihaygndm"

    print("Part 1:", part1(input))
    print("Part 2:", part2(input))


if __name__ == "__main__":
    main()
