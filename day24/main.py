import collections
import itertools


def parse_input(input: str) -> dict[tuple[int, int], str]:
    rows = input.strip().splitlines()

    return {(y, x): rows[y][x] for y in range(len(rows)) for x in range(len(rows[y]))}


def solution(input: str, return_to_zero: bool = False) -> int:
    board = parse_input(input)

    numbers = {i: board[i] for i in board if board[i].isdigit()}
    lengths = {}

    for position, number in numbers.items():
        paths = collections.deque([[position]])
        seen = {position}

        while paths:
            current_path = paths.popleft()
            last_position = current_path[-1]

            if last_position in numbers and len(current_path) > 1:
                lengths[(number, numbers[last_position])] = len(current_path) - 1

            y, x = last_position

            for next_position in ((y + 1, x), (y - 1, x), (y, x + 1), (y, x - 1)):
                if board.get(next_position) != "#" and next_position not in seen:
                    paths.append(current_path + [next_position])
                    seen.add(next_position)

    if return_to_zero:
        build_path = lambda path: ("0", *path, "0")
    else:
        build_path = lambda path: ("0", *path)

    number_options = [i for i in numbers.values() if i != "0"]

    return min(
        sum(lengths[i] for i in itertools.pairwise(build_path(path)))
        for path in itertools.permutations(number_options)
    )


def part1(input: str) -> int:
    return solution(input)


def part2(input: str) -> int:
    return solution(input, return_to_zero=True)


def main() -> None:
    with open("input.txt") as file:
        input = file.read()

    print("Part 1:", part1(input))
    print("Part 2:", part2(input))


if __name__ == "__main__":
    main()
