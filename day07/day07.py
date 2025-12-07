import sys
from functools import lru_cache

Grid = list[str]


def p2(grid: Grid) -> int:

    @lru_cache
    def count_timelines(x: int, y: int) -> int:
        if y == len(grid) - 1:
            return 1

        return (
            count_timelines(x - 1, y + 1) + count_timelines(x + 1, y + 1)
            if grid[y + 1][x] == "^"
            else count_timelines(x, y + 1)
        )

    sx, sy = grid[0].index("S"), 0
    return count_timelines(sx, sy)


def p1(grid: Grid) -> int:
    sx, sy = grid[0].index("S"), 0
    beams = {(sx, sy)}
    splits = 0
    for i in range(len(grid[:-1])):
        new_beams: set[tuple[int, int]] = set()
        for x, y in beams:
            if grid[y + 1][x] == "^":
                splits += 1
                new_beams.add((x - 1, y + 1))
                new_beams.add((x + 1, y + 1))
            else:
                new_beams.add((x, y + 1))

        beams = new_beams

    return splits


def run(filename: str):
    grid = open(filename).read().strip().split("\n")
    print(p1(grid))
    print(p2(grid))


filename = sys.argv[1] if len(sys.argv) > 1 else "test"
run(filename)
