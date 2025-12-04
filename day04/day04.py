import sys
from typing import Iterator

Grid = list[list[str]]


def get_adjacent(grid: Grid, x: int, y: int) -> list[str]:
    nbs: list[str] = []
    c = 0
    for dx in (-1, 0, 1):
        for dy in (-1, 0, 1):
            if not dx and not dy:
                continue
            c += 1

            ny = y + dy
            nx = x + dx

            if not (0 <= ny < len(grid)):
                continue
            if not (0 <= nx < len(grid[ny])):
                continue

            nbs.append(grid[ny][nx])

    return nbs


def can_be_removed(grid: Grid, x: int, y: int) -> bool:
    if grid[y][x] != "@":
        return False

    nbs = get_adjacent(grid, x, y)
    return nbs.count("@") < 4


def get_roll_locations(grid: Grid) -> Iterator[tuple[int, int]]:
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == "@":
                yield x, y


def p1(grid: Grid) -> int:
    return sum(can_be_removed(grid, x, y) for x, y in get_roll_locations(grid))


def p2(grid: Grid) -> int:
    grid = grid.copy()
    roll_locations = list(get_roll_locations(grid))
    removed_rolls = 0
    while True:
        remaining_roll_locations: list[tuple[int, int]] = []
        for x, y in roll_locations[::]:
            if can_be_removed(grid, x, y):
                grid[y][x] = "."
            else:
                remaining_roll_locations.append((x, y))

        if len(remaining_roll_locations) == len(roll_locations):
            break

        removed_rolls += len(roll_locations) - len(remaining_roll_locations)
        roll_locations = remaining_roll_locations

    return removed_rolls


def run(filename: str):
    grid = [list(line) for line in open(filename).read().strip().split("\n")]
    print(p1(grid))
    print(p2(grid))


filename = sys.argv[1] if len(sys.argv) > 1 else "test"
run(filename)
