import re
import sys


def is_valid_p1(id: int) -> bool:
    id_str = str(id)
    if len(id_str) % 2 == 1:
        return True

    mid = len(id_str) // 2
    return id_str[:mid] != id_str[mid:]


def is_valid_p2(id: int) -> bool:
    id_str = str(id)
    for i in range(1, len(id_str) // 2 + 1):
        prefix = id_str[:i]
        rem = re.sub(prefix, "", id_str)
        if not rem:
            return False

    return True


def run(filename: str):
    ranges = [
        tuple(map(int, i.split("-"))) for i in open(filename).read().strip().split(",")
    ]
    invalid_sums_p1 = 0
    for l, h in ranges:
        invalid_sums_p1 += sum(i for i in range(l, h + 1) if not is_valid_p1(i))

    print(invalid_sums_p1)

    invalid_sums_p2 = 0
    for l, h in ranges:
        invalid_sums_p2 += sum(i for i in range(l, h + 1) if not is_valid_p2(i))

    print(invalid_sums_p2)


filename = sys.argv[1] if len(sys.argv) > 1 else "test"
run(filename)
