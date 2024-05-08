import collections
import dataclasses
import re
from typing import DefaultDict, Iterator


@dataclasses.dataclass
class Value:
    value: int


@dataclasses.dataclass
class Bot(Value):
    pass


@dataclasses.dataclass
class Output(Value):
    pass


class Instruction:
    pass


@dataclasses.dataclass
class Init(Instruction):
    value: int
    bot: int


@dataclasses.dataclass
class Give(Instruction):
    bot: int
    low: Value
    high: Value


def parse_input(input: str) -> list[Instruction]:
    instructions: list[Instruction] = []

    for line in input.strip().splitlines():
        if match := re.match(r"value (\d+) goes to bot (\d+)", line):
            instructions.append(Init(int(match.group(1)), int(match.group(2))))
        elif match := re.match(
            r"bot (\d+) gives low to (\w+) (\d+) and high to (\w+) (\d+)", line
        ):
            low_value = int(match.group(3))
            low = Bot(low_value) if match.group(2) == "bot" else Output(low_value)
            high_value = int(match.group(5))
            high = Bot(high_value) if match.group(4) == "bot" else Output(high_value)
            instructions.append(Give(int(match.group(1)), low, high))
        else:
            raise ValueError(f"Invalid {line}")

    return instructions


def solution(input: str) -> Iterator[tuple[int, int, int] | int]:
    instructions = parse_input(input)

    bots: DefaultDict[int, list[int]] = collections.defaultdict(list)
    bot_instructions: DefaultDict[int, list[Give]] = collections.defaultdict(list)

    for i in instructions:
        if isinstance(i, Init):
            bots[i.bot].append(i.value)
        elif isinstance(i, Give):
            bot_instructions[i.bot].append(i)

    outputs = collections.defaultdict(list)

    while (bot := next((i for i in bots if len(bots[i]) == 2), None)) is not None:
        instruction = bot_instructions[bot].pop(0)
        lower, higher = sorted([bots[bot].pop(), bots[bot].pop()])

        if (lower, higher):
            yield lower, higher, bot

        if isinstance(instruction.low, Output):
            outputs[instruction.low.value].append(lower)
        else:
            bots[instruction.low.value].append(lower)

        if isinstance(instruction.high, Output):
            outputs[instruction.high.value].append(higher)
        else:
            bots[instruction.high.value].append(higher)

    yield outputs[0][0] * outputs[1][0] * outputs[2][0]


def part1(input: str, lower_value: int = 17, higher_value: int = 61) -> int:
    return next(
        i[2]
        for i in solution(input)
        if isinstance(i, tuple) and i[0] == lower_value and i[1] == higher_value
    )


def part2(input: str) -> int:
    return next(i for i in solution(input) if isinstance(i, int))


def main() -> None:
    with open("input.txt") as file:
        input = file.read()

    print("Part 1:", part1(input))
    print("Part 2:", part2(input))


if __name__ == "__main__":
    main()
