import collections
import enum


class Face(enum.IntEnum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3


FACES = {
    Face.NORTH: (1, 0),
    Face.EAST: (0, 1),
    Face.SOUTH: (-1, 0),
    Face.WEST: (0, -1),
}


class Turn(enum.StrEnum):
    RIGHT = "R"
    LEFT = "L"


def parse_input(input: str) -> list[tuple[Turn, int]]:
    return [(Turn(i[0]), int(i[1:])) for i in input.strip().split(", ")]


def solution(input: str, stop_visit_twice: bool) -> int:
    instructions = parse_input(input)

    faces = collections.deque(Face)

    how_far = lambda y, x: sum(map(abs, (y, x)))

    y, x = 0, 0

    visited = {(0, 0)}

    for turn, i in instructions:
        if turn == Turn.LEFT:
            faces.rotate(1)
        else:
            faces.rotate(-1)

        face = FACES[faces[0]]

        for _ in range(i):
            y += face[0]
            x += face[1]

            if stop_visit_twice and (y, x) in visited:
                return how_far(y, x)

            visited.add((y, x))

    return how_far(y, x)


def part1(input: str) -> int:
    return solution(input, stop_visit_twice=False)


def part2(input: str) -> int:
    return solution(input, stop_visit_twice=True)


def main() -> None:
    with open("input.txt") as file:
        input = file.read()

    print("Part 1:", part1(input))
    print("Part 2:", part2(input))


if __name__ == "__main__":
    main()
