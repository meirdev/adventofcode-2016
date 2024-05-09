import dataclasses
import re


@dataclasses.dataclass(frozen=True)
class Component:
    name: str


@dataclasses.dataclass(frozen=True)
class Generator(Component):
    def __str__(self) -> str:
        return f"{self.name[:2].upper()}G"


@dataclasses.dataclass(frozen=True)
class Microchip(Component):
    def __str__(self) -> str:
        return f"{self.name[:2].upper()}M"


def parse_input(input: str) -> dict[int, set[Component]]:
    floors = {}

    for floor, line in enumerate(input.strip().splitlines(), start=1):
        components = set()

        for name, type_ in re.findall(
            r"(\w+)((?: generator)|(?:-compatible microchip))", line
        ):
            cls = Generator if "generator" in type_ else Microchip
            components.add(cls(name))

        floors[floor] = components

    return floors


def solution(floors: dict[int, set[Component]]) -> int:
    return -1


def part1(input: str) -> int:
    floors = parse_input(input)

    return solution(floors)


def part2(input: str) -> int:
    floors = parse_input(input)

    floors[1] |= {
        Generator("elerium"),
        Microchip("elerium"),
        Generator("dilithium"),
        Microchip("dilithium"),
    }

    return solution(floors)


def main() -> None:
    with open("input.txt") as file:
        input = file.read()

    print("Part 1:", part1(input))
    print("Part 2:", part2(input))


if __name__ == "__main__":
    main()
