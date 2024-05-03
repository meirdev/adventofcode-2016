import hashlib
import itertools
from typing import Iterator


def generate_hash(input: str) -> Iterator[str]:
    for i in itertools.count(0):
        md5 = hashlib.md5()
        md5.update(f"{input}{i}".encode())

        hex = md5.hexdigest()

        if hex[:5] == "00000":
            yield hex


def part1(input: str) -> str:
    hash_iter = generate_hash(input)

    return "".join(next(hash_iter)[5] for _ in range(8))


def part2(input: str) -> str:
    hash_iter = generate_hash(input)

    password: dict[str, str] = {}

    while len(password) < 8:
        hash = next(hash_iter)

        if "0" <= hash[5] < "8" and hash[5] not in password:
            password[hash[5]] = hash[6]

    return "".join(password[i] for i in sorted(password))


def main() -> None:
    input = "abbhdwsy"

    print("Part 1:", part1(input))
    print("Part 2:", part2(input))


if __name__ == "__main__":
    main()
