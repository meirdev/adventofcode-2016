import collections
import dataclasses
from typing import DefaultDict, TypeAlias


Register: TypeAlias = str

Value: TypeAlias = int | Register


@dataclasses.dataclass
class Instruction:
    pass


@dataclasses.dataclass
class cpy(Instruction):
    value: Value
    register: Register


@dataclasses.dataclass
class inc(Instruction):
    register: Register


@dataclasses.dataclass
class dec(Instruction):
    register: Register


@dataclasses.dataclass
class jnz(Instruction):
    value: Value
    jump: int


def parse_input(input: str) -> list[Instruction]:
    instructions: list[Instruction] = []

    for line in input.strip().splitlines():
        match line.split(" "):
            case ["inc", reg]:
                instructions.append(inc(reg))
            case ["dec", reg]:
                instructions.append(dec(reg))
            case ["cpy", val, reg]:
                instructions.append(cpy(int(val) if val.isdigit() else val, reg))
            case ["jnz", val, jump]:
                instructions.append(jnz(int(val) if val.isdigit() else val, int(jump)))

    return instructions


def solution(input: str, **default_registers: int) -> int:
    instructions = parse_input(input)

    registers: DefaultDict[str, int] = collections.defaultdict(int)
    registers |= default_registers

    i = 0

    while i < len(instructions):
        match instructions[i]:
            case cpy(val, reg):
                registers[reg] = val if isinstance(val, int) else registers[val]
            case inc(reg):
                registers[reg] += 1
            case dec(reg):
                registers[reg] -= 1
            case jnz(val, jump):
                if (val if isinstance(val, int) else registers[val]) != 0:
                    i += jump
                    continue

        i += 1

    return registers["a"]


def part1(input: str) -> int:
    return solution(input)


def part2(input: str) -> int:
    return solution(input, c=1)


def main() -> None:
    with open("input.txt") as file:
        input = file.read()

    print("Part 1:", part1(input))
    print("Part 2:", part2(input))


if __name__ == "__main__":
    main()
