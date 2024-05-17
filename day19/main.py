import collections


def part1(input: int) -> int:
    elves = collections.deque([(i, 1) for i in range(1, input + 1)])

    while len(elves) > 1:
        for _ in range(len(elves) // 2):
            a, b = elves.popleft(), elves.popleft()

            elves.appendleft((a[0], a[1] + b[1]))

            elves.rotate(-1)

    return elves[0][0]


def part2(input: int) -> int:
    i = 1

    while i * 3 < input:
        i *= 3

    return input - i


def main() -> None:
    input = 3005290

    print("Part 1:", part1(input))
    print("Part 2:", part2(input))


if __name__ == "__main__":
    main()
