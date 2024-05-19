import collections
import re
from typing import NamedTuple, Protocol


class Operation(Protocol):
    def apply(self, s: list[str]) -> None: ...

    def reverse(self, s: list[str]) -> None: ...


class SwapPositions(NamedTuple):
    x: int
    y: int

    def apply(self, s: list[str]) -> None:
        s[self.x], s[self.y] = s[self.y], s[self.x]

    def reverse(self, s: list[str]) -> None:
        self.apply(s)


class SwapLetters(NamedTuple):
    x: str
    y: str

    def apply(self, s: list[str]) -> None:
        for i, char in enumerate(s):
            if char == self.x:
                s[i] = self.y
            elif char == self.y:
                s[i] = self.x

    def reverse(self, s: list[str]) -> None:
        self.apply(s)


class RotateLeft(NamedTuple):
    x: int

    def apply(self, s: list[str]) -> None:
        temp = collections.deque(s)
        temp.rotate(-self.x)

        for i in range(len(s)):
            s[i] = temp[i]

    def reverse(self, s: list[str]) -> None:
        RotateRight(self.x).apply(s)


class RotateRight(NamedTuple):
    x: int

    def apply(self, s: list[str]) -> None:
        temp = collections.deque(s)
        temp.rotate(self.x)

        for i in range(len(s)):
            s[i] = temp[i]

    def reverse(self, s: list[str]) -> None:
        RotateLeft(self.x).apply(s)


class RotatePosition(NamedTuple):
    x: str

    def apply(self, s: list[str]) -> None:
        i = s.index(self.x)

        RotateRight(1 + i + int(i >= 4)).apply(s)

    def reverse(self, s: list[str]) -> None:
        for i in range(1, len(s)):
            temp = s[:]
            RotateLeft(i).apply(temp)
            self.apply(temp)
            if temp == s:
                RotateLeft(i).apply(s)
                return


class ReversePositions(NamedTuple):
    x: int
    y: int

    def apply(self, s: list[str]) -> None:
        s[self.x : self.y + 1] = s[self.x : self.y + 1][::-1]

    def reverse(self, s: list[str]) -> None:
        self.apply(s)


class MovePositions(NamedTuple):
    x: int
    y: int

    def apply(self, s: list[str]) -> None:
        s.insert(self.y, s.pop(self.x))

    def reverse(self, s: list[str]) -> None:
        s.insert(self.x, s.pop(self.y))


def parse_input(input: str) -> list[Operation]:
    operations: list[Operation] = []

    for line in input.strip().splitlines():
        operation: Operation

        if match := re.match(r"swap position (\d+) with position (\d+)", line):
            operation = SwapPositions(int(match.group(1)), int(match.group(2)))
        elif match := re.match(r"swap letter (\w) with letter (\w)", line):
            operation = SwapLetters(match.group(1), match.group(2))
        elif match := re.match(r"rotate left (\d+) steps?", line):
            operation = RotateLeft(int(match.group(1)))
        elif match := re.match(r"rotate right (\d+) steps?", line):
            operation = RotateRight(int(match.group(1)))
        elif match := re.match(r"rotate based on position of letter (\w)", line):
            operation = RotatePosition(match.group(1))
        elif match := re.match(r"reverse positions (\d+) through (\d+)", line):
            operation = ReversePositions(int(match.group(1)), int(match.group(2)))
        elif match := re.match(r"move position (\d+) to position (\d+)", line):
            operation = MovePositions(int(match.group(1)), int(match.group(2)))
        else:
            raise ValueError(f"unknown operation: {line}")

        operations.append(operation)

    return operations


def part1(input: str, password: str = "abcdefgh"):
    operations = parse_input(input)

    password_list = list(password)

    for op in operations:
        op.apply(password_list)

    return "".join(password_list)


def part2(input: str, password: str = "fbgdceah"):
    operations = parse_input(input)

    password_list = list(password)

    for op in reversed(operations):
        op.reverse(password_list)

    return "".join(password_list)


def main() -> None:
    with open("input.txt") as file:
        input = file.read()

    print("Part 1:", part1(input))
    print("Part 2:", part2(input))


if __name__ == "__main__":
    main()
