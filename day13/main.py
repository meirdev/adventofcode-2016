import enum
import functools
from typing import Callable, Iterator, TypeAlias


Location: TypeAlias = tuple[int, int]

Path: TypeAlias = set[Location]


class LocationType(enum.IntEnum):
    WALL = 0
    OPEN_SPACE = 1


@functools.cache
def detect_type(favorite_number: int, y: int, x: int) -> LocationType:
    return (
        LocationType.OPEN_SPACE
        if (x * x + 3 * x + 2 * x * y + y + y * y + favorite_number).bit_count() % 2
        == 0
        else LocationType.WALL
    )


def get_paths(
    input: str, stop: Callable[[Location, Path], bool]
) -> Iterator[Path | Location]:
    favorite_number = parse_input(input)

    def rec(location: Location, path: Path):
        if stop(location, path):
            yield path
            return

        yield location

        y, x = location

        for y, x in ((y - 1, x), (y + 1, x), (y, x - 1), (y, x + 1)):
            if (
                y >= 0
                and x >= 0
                and detect_type(favorite_number, y, x) == LocationType.OPEN_SPACE
                and (y, x) not in path
            ):
                yield from rec((y, x), path | {(y, x)})

    yield from rec((1, 1), {(1, 1)})


def parse_input(input: str) -> int:
    return int(input)


def part1(input: str, dest: Location = (39, 31)) -> int:
    return min(
        len(i) - 1
        for i in get_paths(input, lambda location, _: location == dest)
        if isinstance(i, set)
    )


def part2(input: str) -> int:
    return len(
        {
            i
            for i in get_paths(input, lambda _, path: len(path) - 1 > 50)
            if isinstance(i, tuple)
        }
    )


def main() -> None:
    input = "1358"

    print("Part 1:", part1(input))
    print("Part 2:", part2(input))


if __name__ == "__main__":
    main()
