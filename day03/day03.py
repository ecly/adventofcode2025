import sys


def get_max_joltage(
    bank: list[int], batteries: int = 2, selected: list[int] | None = None
) -> int:
    selectable = bank[: -(batteries - 1)] if batteries > 1 else bank
    b = max(selectable)
    bi = selectable.index(b)
    rem = bank[bi + 1 :]
    selected = selected + [b] if selected else [b]
    if batteries > 1:
        return get_max_joltage(rem, batteries=batteries - 1, selected=selected)

    return int("".join(str(i) for i in selected))


def run(filename: str):
    banks = [list(map(int, line)) for line in open(filename).read().strip().split("\n")]
    print(sum(get_max_joltage(bank) for bank in banks))
    print(sum(get_max_joltage(bank, 12) for bank in banks))


filename = sys.argv[1] if len(sys.argv) > 1 else "test"
run(filename)
