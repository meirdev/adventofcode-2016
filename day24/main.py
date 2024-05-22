def parse_input(input: str) -> dict[tuple[int, int], str]:
    rows = input.strip().splitlines()

    return {
        (y, x): rows[y][x]
        for y in range(len(rows))
        for x in range(len(rows[y]))
        if rows[y][x] != "#"
    }


def part1(input: str) -> int:
    pass


def part2(input: str) -> int:
    pass


def main() -> None:
    with open("input.txt") as file:
        input = file.read()

    print("Part 1:", part1(input))
    print("Part 2:", part2(input))


if __name__ == "__main__":
    main()
