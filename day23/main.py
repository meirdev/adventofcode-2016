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


@dataclasses.dataclass
class tgl(Instruction):
    value: Value


@dataclasses.dataclass
class mul(Instruction):
    value1: Value
    value2: Value
    register: Register


FIND = """\
cpy b c
inc a
dec c
jnz c -2
dec d
jnz d -5"""

REPLACE = """\
mul b d a
cpy 0 c
cpy 0 d
jnz 0 0
jnz 0 0
jnz 0 0"""


def parse_input(input: str) -> list[Instruction]:
    instructions: list[Instruction] = []

    def get_value(val: str) -> Value:
        return val if val.isalpha() else int(val)

    for line in input.strip().splitlines():
        match line.split(" "):
            case ["mul", val1, val2, reg]:
                instructions.append(mul(get_value(val1), get_value(val2), reg))
            case ["tgl", val]:
                instructions.append(tgl(get_value(val)))
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
    input = input.replace(FIND, REPLACE)

    instructions = parse_input(input)

    registers: DefaultDict[str, int] = collections.defaultdict(int)
    registers |= default_registers

    def get_value(val: Value) -> int:
        return val if isinstance(val, int) else registers[val]

    i = 0

    while i < len(instructions):
        match instructions[i]:
            case mul(val1, val2, reg):
                registers[reg] = get_value(val1) * get_value(val2)
            case tgl(val):
                target = get_value(val) + i

                if 0 <= target < len(instructions):
                    match instructions[target]:
                        case inc(reg):
                            instructions[target] = dec(reg)
                        case dec(reg):
                            instructions[target] = inc(reg)
                        case tgl(val):
                            instructions[target] = inc(val)  # type: ignore
                        case jnz(val, jump):
                            instructions[target] = cpy(val, jump)  # type: ignore
                        case cpy(val, reg):
                            instructions[target] = jnz(val, reg)
            case cpy(val, reg):
                if not isinstance(reg, int):
                    registers[reg] = get_value(val)
            case inc(reg):
                if not isinstance(reg, int):
                    registers[reg] += 1
            case dec(reg):
                if not isinstance(reg, int):
                    registers[reg] -= 1
            case jnz(val, jump):
                if get_value(val) != 0:
                    i += get_value(jump)
                    continue

        i += 1

    return registers["a"]


def part1(input: str) -> int:
    return solution(input, a=7)


def part2(input: str) -> int:
    return solution(input, a=12)


def main() -> None:
    with open("input.txt") as file:
        input = file.read()

    print("Part 1:", part1(input))
    print("Part 2:", part2(input))


if __name__ == "__main__":
    main()
