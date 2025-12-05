from collections import deque
from pathlib import Path


SIDES = [
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (0, -1),
    (0, 1),
    (1, -1),
    (1, 0),
    (1, 1),
]


def count_accessible_rolls(grid: list[str]) -> int:
    rows = len(grid)
    cols = len(grid[0]) if rows else 0
    total = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != "@":
                continue
            neighbors = 0
            for dr, dc in SIDES:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "@":
                    neighbors += 1
            if neighbors < 4:
                total += 1
    return total


def total_removed_rolls(grid_lines: list[str]) -> int:
    grid = [list(row) for row in grid_lines]
    rows = len(grid)
    cols = len(grid[0]) if rows else 0

    deg = [[0] * cols for _ in range(rows)]
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != "@":
                continue
            count = 0
            for dr, dc in SIDES:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "@":
                    count += 1
            deg[r][c] = count

    q: deque[tuple[int, int]] = deque()
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "@" and deg[r][c] < 4:
                q.append((r, c))

    removed = 0
    while q:
        r, c = q.popleft()
        if grid[r][c] != "@":
            continue
        grid[r][c] = "."
        removed += 1
        for dr, dc in SIDES:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "@":
                deg[nr][nc] -= 1
                if deg[nr][nc] < 4:
                    q.append((nr, nc))

    return removed


def main() -> None:
    input_path = Path(__file__).with_name("input")
    lines = [line for line in input_path.read_text().strip().splitlines() if line]
    part1 = count_accessible_rolls(lines)
    part2 = total_removed_rolls(lines)
    print(part1)
    print(part2)


if __name__ == "__main__":
    main()
