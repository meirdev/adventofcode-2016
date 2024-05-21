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
    jump: Value


def parse_input(input: str) -> list[Instruction]:
    instructions: list[Instruction] = []

    def get_value(val: str) -> Value:
        return val if val.isalpha() else int(val)

    for line in input.strip().splitlines():
        match line.split(" "):
            case ["inc", reg]:
                instructions.append(inc(reg))
            case ["dec", reg]:
                instructions.append(dec(reg))
            case ["cpy", val, reg]:
                instructions.append(cpy(get_value(val), reg))
            case ["jnz", val, jump]:
                instructions.append(jnz(get_value(val), get_value(jump)))

    return instructions


def solution(input: str, **default_registers: int) -> int:
    instructions = parse_input(input)

    registers: DefaultDict[str, int] = collections.defaultdict(int)
    registers |= default_registers

    def get_value(val: Value) -> int:
        return val if isinstance(val, int) else registers[val]

    i = 0

    while i < len(instructions):
        match instructions[i]:
            case cpy(val, reg):
                registers[reg] = get_value(val)
            case inc(reg):
                registers[reg] += 1
            case dec(reg):
                registers[reg] -= 1
            case jnz(val, jump):
                if get_value(val) != 0:
                    i += get_value(jump)
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
