import collections
import re
from typing import NamedTuple


class Room(NamedTuple):
    name: str
    sector_id: int
    checksum: str


def parse_input(input: str) -> list[Room]:
    return [
        Room(i[0], int(i[1]), i[2])
        for i in re.findall(r"([a-z\-]+)-(\d+)\[(.+?)\]", input)
    ]


def decrypt(room: Room) -> str:
    decrypted = []

    for i in room.name:
        if i == "-":
            decrypted.append(" ")
        else:
            c = ord(i) + (room.sector_id % 26)

            if c > ord("z"):
                decrypted.append(chr(c - ord("z") + ord("a") - 1))
            else:
                decrypted.append(chr(c))

    return "".join(decrypted)


def is_real(room: Room) -> bool:
    letters = collections.Counter(i for i in room.name if i != "-")

    for i in room.checksum:
        if letters[i] == max(letters.values()):
            del letters[i]
        else:
            break
    else:
        return True

    return False


def part1(input: str) -> int:
    rooms = parse_input(input)

    return sum(i.sector_id for i in rooms if is_real(i))


def part2(input: str) -> int:
    rooms = parse_input(input)

    return next(i.sector_id for i in rooms if "northpole" in decrypt(i))


def main() -> None:
    with open("input.txt") as file:
        input = file.read()

    print("Part 1:", part1(input))
    print("Part 2:", part2(input))


if __name__ == "__main__":
    main()
