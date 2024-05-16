import enum
import functools


class Tile(enum.StrEnum):
    SAFE = "."
    TRAP = "^"


def parse_input(input: str) -> list[Tile]:
    return list(map(Tile, input.strip()))


@functools.cache
def is_trap(t: tuple[Tile | None]) -> bool:
    return t in (
        (Tile.TRAP, Tile.TRAP, Tile.SAFE),
        (Tile.TRAP, Tile.TRAP, None),
        (Tile.SAFE, Tile.TRAP, Tile.TRAP),
        (None, Tile.TRAP, Tile.TRAP),
        (Tile.TRAP, Tile.SAFE, Tile.SAFE),
        (Tile.TRAP, Tile.SAFE, None),
        (Tile.SAFE, Tile.SAFE, Tile.TRAP),
        (None, Tile.SAFE, Tile.TRAP),
    )


def solution(input: str, rows: int) -> int:
    tiles = parse_input(input)

    width = len(tiles)

    safes = tiles.count(Tile.SAFE)

    for _ in range(rows - 1):
        next = [
            (
                Tile.TRAP
                if is_trap(
                    (
                        None if i == 0 else tiles[i - 1],
                        tiles[i],
                        None if i == width - 1 else tiles[i + 1],
                    )
                )
                else Tile.SAFE
            )
            for i in range(width)
        ]

        safes += next.count(Tile.SAFE)

        tiles = next

    return safes


def part1(input: str, rows: int = 40) -> int:
    return solution(input, rows)


def part2(input: str) -> int:
    return solution(input, 400000)


def main() -> None:
    with open("input.txt") as file:
        input = file.read()

    print("Part 1:", part1(input))
    print("Part 2:", part2(input))


if __name__ == "__main__":
    main()
