import collections


def parse_input(input: str) -> list[str]:
    return input.strip().splitlines()


def solution(input: str, index: int) -> str:
    messages = parse_input(input)

    return "".join(
        collections.Counter(i).most_common()[index][0] for i in zip(*messages)
    )


def part1(input: str) -> str:
    return solution(input, 0)


def part2(input: str) -> str:
    return solution(input, -1)


def main() -> None:
    with open("input.txt") as file:
        input = file.read()

    print("Part 1:", part1(input))
    print("Part 2:", part2(input))


if __name__ == "__main__":
    main()
