import functools
import itertools
import re
import string

ABBA = [
    f"{i[0]}{i[1]}{i[1]}{i[0]}"
    for i in itertools.permutations(string.ascii_lowercase, r=2)
]

ABA = [
    f"{i[1]}{i[0]}{i[1]}" for i in itertools.permutations(string.ascii_lowercase, r=2)
]

ABA_BAB = {i: f"{i[1]}{i[0]}{i[1]}" for i in ABA}


class Section:
    def __init__(self, s: str) -> None:
        self._s = s

    @property
    def list_abba(self) -> list[str]:
        return [i for i in ABBA if i in self._s]

    @property
    def list_aba(self) -> list[str]:
        return [i for i in ABA if i in self._s]


class Supernet(Section):
    pass


class Hypernet(Section):
    pass


class IPv7:
    def __init__(self, ip: str) -> None:
        sections: list[str] = re.findall(r"\w+|\[\w+\]", ip)

        self._ip = [Hypernet(i) if i.startswith("[") else Supernet(i) for i in sections]

    @property
    def list_hypernet(self) -> list[Hypernet]:
        return [i for i in self._ip if isinstance(i, Hypernet)]

    @property
    def list_supernet(self) -> list[Supernet]:
        return [i for i in self._ip if isinstance(i, Supernet)]

    def is_support_tls(self) -> bool:
        return all(len(i.list_abba) == 0 for i in self.list_hypernet) and any(
            len(i.list_abba) > 0 for i in self.list_supernet
        )

    def is_support_ssl(self) -> bool:
        return (
            len(
                functools.reduce(
                    lambda a, b: a | set(b.list_aba), self.list_hypernet, set[str]()
                )
                & functools.reduce(
                    lambda a, b: a | set(ABA_BAB[i] for i in b.list_aba),
                    self.list_supernet,
                    set[str](),
                )
            )
            > 0
        )


def parse_input(input: str) -> list[IPv7]:
    return list(map(IPv7, input.strip().splitlines()))


def part1(input: str) -> int:
    ips = parse_input(input)

    return sum(map(IPv7.is_support_tls, ips))


def part2(input: str) -> int:
    ips = parse_input(input)

    return sum(map(IPv7.is_support_ssl, ips))


def main() -> None:
    with open("input.txt") as file:
        input = file.read()

    print("Part 1:", part1(input))
    print("Part 2:", part2(input))


if __name__ == "__main__":
    main()
