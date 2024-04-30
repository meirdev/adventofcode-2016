import enum
from typing import TypeAlias

Keypad: TypeAlias = dict[tuple[int, int], str]


class Move(enum.StrEnum):
    UP = "U"
    DOWN = "D"
    LEFT = "L"
    RIGHT = "R"


MOVES = {
    Move.UP: (-1, 0),
    Move.RIGHT: (0, 1),
    Move.DOWN: (1, 0),
    Move.LEFT: (0, -1),
}

KEYPAD_1 = """
1 2 3
4 5 6
7 8 9
"""

KEYPAD_2 = """
    1
  2 3 4
5 6 7 8 9
  A B C
    D
"""


def parse_input(input: str) -> list[list[Move]]:
    return [list(map(Move, row)) for row in input.strip().splitlines()]


def parse_keypad(keypad: str) -> Keypad:
    return {
        (y, x): row[col]
        for y, row in enumerate(keypad.strip("\n").splitlines())
        for x, col in enumerate(range(0, len(row), 2))
        if row[col] != " "
    }


def solution(input: str, keypad: str) -> str:
    move_rows = parse_input(input)

    keypad_dict = parse_keypad(keypad)

    y, x = next(i for i in keypad_dict if keypad_dict[i] == "5")

    bathroom_code = []

    for moves in move_rows:
        for move in moves:
            y_temp, x_temp = y + MOVES[move][0], x + MOVES[move][1]

            if (y_temp, x_temp) not in keypad_dict:
                continue

            y, x = y_temp, x_temp

        bathroom_code.append(keypad_dict[y, x])

    return "".join(bathroom_code)


def part1(input: str) -> str:
    return solution(input, KEYPAD_1)


def part2(input: str) -> str:
    return solution(input, KEYPAD_2)


def main() -> None:
    with open("input.txt") as file:
        input = file.read()

    print("Part 1:", part1(input))
    print("Part 2:", part2(input))


if __name__ == "__main__":
    main()
