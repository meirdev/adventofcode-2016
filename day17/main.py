import enum
import functools
import hashlib


class Direction(enum.StrEnum):
    UP = "U"
    DOWN = "D"
    LEFT = "L"
    RIGHT = "R"


DIRECTIONS = {
    Direction.UP: (-1, 0),
    Direction.DOWN: (1, 0),
    Direction.LEFT: (0, -1),
    Direction.RIGHT: (0, 1),
}


def open_doors(s: str) -> list[Direction]:
    md5 = hashlib.md5()
    md5.update(s.encode())

    return [dir for dir, i in zip(Direction, md5.hexdigest()[:4]) if i in "bcdef"]  # type: ignore


@functools.cache
def solution(input: str) -> tuple[str, str]:
    min_max = ["", ""]

    def rec(y: int, x: int, input_: str) -> None:
        if y == 3 and x == 3:
            if min_max[0] == "" or len(input_) < len(min_max[0]):
                min_max[0] = input_
            if min_max[1] == "" or len(input_) > len(min_max[1]):
                min_max[1] = input_
            return

        for i, y_, x_ in (
            (i, y + DIRECTIONS[i][0], x + DIRECTIONS[i][1])
            for i in open_doors(input + input_)
        ):
            if 0 <= y_ < 4 and 0 <= x_ < 4:
                rec(y_, x_, input_ + str(i))

    rec(0, 0, "")

    return tuple(min_max)  # type: ignore


def part1(input: str) -> str:
    return solution(input)[0]


def part2(input: str) -> int:
    return len(solution(input)[1])


def main() -> None:
    input = "mmsxrhfx"

    print("Part 1:", part1(input))
    print("Part 2:", part2(input))


if __name__ == "__main__":
    main()
