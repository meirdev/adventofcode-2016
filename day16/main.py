import itertools


def solution(input: str, disk_length: int) -> str:
    input_list = list(input)

    while len(input_list) < disk_length:
        input_list += ["0", *("0" if i == "1" else "1" for i in reversed(input_list))]

    checksum = input_list[:disk_length]

    while len(checksum) % 2 == 0:
        checksum = ["1" if a == b else "0" for a, b in itertools.batched(checksum, 2)]

    return "".join(checksum)


def part1(input: str, disk_length: int = 272) -> str:
    return solution(input, disk_length)


def part2(input: str) -> str:
    return solution(input, 35651584)


def main() -> None:
    input = "10001110011110000"

    print("Part 1:", part1(input))
    print("Part 2:", part2(input))


if __name__ == "__main__":
    main()
