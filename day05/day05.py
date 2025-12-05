import sys
from collections import deque
from typing import cast


def is_fresh(ingredient: int, fresh_ranges: list[tuple[int, int]]) -> bool:
    return any(lo <= ingredient <= hi for lo, hi in fresh_ranges)


def merge_ranges(ranges: list[tuple[int, int]]) -> list[tuple[int, int]]:
    merged: list[tuple[int, int]] = []
    seen: set[tuple[int, int]] = set()

    ranges = sorted(ranges)
    queue = deque(ranges)
    while queue:
        lo, hi = queue.popleft()
        if (lo, hi) in seen:
            continue

        seen.add((lo, hi))
        for nlo, nhi in ranges:
            if hi < nlo:
                break

            if (nlo, nhi) in seen:
                continue

            if lo > nhi:
                continue

            lo, hi = min(lo, nlo), max(hi, nhi)
            seen.add((nlo, nhi))

        merged.append((lo, hi))

    return merged


def p2(ranges: list[tuple[int, int]]) -> int:
    ranges = merge_ranges(ranges)
    print(ranges)
    return sum(hi - lo for lo, hi in ranges) + len(ranges)


def p1(ingredients: list[int], fresh_ranges: list[tuple[int, int]]) -> int:
    return sum(is_fresh(i, fresh_ranges) for i in ingredients)


def run(filename: str):
    fresh_ranges_str, ingredients_str = open(filename).read().strip().split("\n\n")
    fresh_ranges = cast(
        list[tuple[int, int]],
        [tuple(map(int, line.split("-"))) for line in fresh_ranges_str.split("\n")],
    )
    ingredients = [int(line) for line in ingredients_str.split("\n")]
    print(p1(ingredients, fresh_ranges))
    print(p2(fresh_ranges))


filename = sys.argv[1] if len(sys.argv) > 1 else "test"
run(filename)
