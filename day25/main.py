import dataclasses
from typing import TypeAlias, cast


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
class out(Instruction):
    value: Value


def parse_input(input: str) -> list[Instruction]:
    instructions: list[Instruction] = []

    def get_value(val: str) -> Value:
        return val if val.isalpha() else int(val)

    for line in input.strip().splitlines():
        match line.split(" "):
            case ["out", val]:
                instructions.append(out(get_value(val)))
            case ["inc", reg]:
                instructions.append(inc(reg))
            case ["dec", reg]:
                instructions.append(dec(reg))
            case ["cpy", val, reg]:
                instructions.append(cpy(get_value(val), reg))
            case ["jnz", val, jump]:
                instructions.append(jnz(get_value(val), get_value(jump)))

    return instructions


def part1(input: str) -> int:
    instructions = parse_input(input)

    c = cast(int, cast(cpy, instructions[1]).value)
    b = cast(int, cast(cpy, instructions[2]).value)

    target = c * b

    n = 1

    while n < target:
        if n % 2 == 0:
            n = n * 2 + 1
        else:
            n *= 2

    return n - target


def main() -> None:
    with open("input.txt") as file:
        input = file.read()

    print("Part 1:", part1(input))


if __name__ == "__main__":
    main()
