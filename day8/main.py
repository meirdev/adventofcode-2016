import collections
import dataclasses
import enum
import itertools
import re
from typing import Any, Type


class Light(enum.Flag):
    ON = True
    OFF = False


class Operation:
    pass


@dataclasses.dataclass
class Rect(Operation):
    width: int
    height: int


@dataclasses.dataclass
class RotateRow(Operation):
    row: int
    right: int


@dataclasses.dataclass
class RotateColumn(Operation):
    column: int
    down: int


def rotate(list_: list[Any], n: int) -> list[Any]:
    deque = collections.deque(list_)
    deque.rotate(n)
    return list(deque)


class Screen:
    def __init__(self, width: int, height: int) -> None:
        self._width = width
        self._height = height

        self._screen = [[Light.OFF] * width for _ in range(height)]

    def __str__(self) -> str:
        return "\n".join(
            "".join(
                "#" if self._screen[y][x] == Light.ON else "."
                for x in range(self._width)
            )
            for y in range(self._height)
        )

    @property
    def lit(self) -> int:
        return sum(light == Light.ON for row in self._screen for light in row)

    def do(self, op: Operation) -> None:
        match op:
            case Rect(width, height):
                for y, x in itertools.product(range(height), range(width)):
                    self._screen[y][x] = Light.ON

            case RotateRow(row, right):
                self._screen[row] = rotate(self._screen[row], right)

            case RotateColumn(column, down):
                for screen_row, val in zip(
                    self._screen, rotate([row[column] for row in self._screen], down)
                ):
                    screen_row[column] = val


def parse_input(input: str) -> list[Operation]:
    operations: list[Operation] = []

    for i in input.strip().splitlines():
        op_type: Type[Rect | RotateRow | RotateColumn]

        if match := re.match(r"rect (\d+)x(\d+)", i):
            op_type = Rect
        elif match := re.match(r"rotate row y=(\d+) by (\d+)", i):
            op_type = RotateRow
        elif match := re.match(r"rotate column x=(\d+) by (\d+)", i):
            op_type = RotateColumn
        else:
            raise ValueError(f"Invalid {i}")

        operations.append(op_type(int(match.group(1)), int(match.group(2))))

    return operations


def solution(input: str, screen_size: tuple[int, int]) -> Screen:
    operations = parse_input(input)

    screen = Screen(screen_size[0], screen_size[1])

    for op in operations:
        screen.do(op)

    return screen


def part1(input: str, screen_size: tuple[int, int] = (50, 6)) -> int:
    return solution(input, screen_size).lit


def part2(input: str, screen_size: tuple[int, int] = (50, 6)) -> str:
    return "\n" + str(solution(input, screen_size))


def main() -> None:
    with open("input.txt") as file:
        input = file.read()

    print("Part 1:", part1(input))
    print("Part 2:", part2(input))


if __name__ == "__main__":
    main()
