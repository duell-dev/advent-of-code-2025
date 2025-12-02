from pathlib import Path


def parse_rotations(raw: str) -> list[tuple[str, int]]:
    rotations: list[tuple[str, int]] = []
    for line in raw.splitlines():
        line = line.strip()
        if not line:
            continue
        direction = line[0]
        distance = int(line[1:])
        if direction not in ("L", "R"):
            raise ValueError(f"Unexpected direction {direction!r}")
        rotations.append((direction, distance))
    return rotations


def count_zero_hits(rotations: list[tuple[str, int]], start: int = 50, size: int = 100) -> int:
    position = start
    hits = 0
    for direction, distance in rotations:
        if direction == "R":
            position = (position + distance) % size
        else:
            position = (position - distance) % size
        if position == 0:
            hits += 1
    return hits


def count_zero_hits_per_click(
    rotations: list[tuple[str, int]], start: int = 50, size: int = 100
) -> int:
    position = start
    hits = 0
    for direction, distance in rotations:
        if direction == "R":
            first_hit = (size - position) % size
            if first_hit == 0:
                first_hit = size
            if distance >= first_hit:
                hits += 1 + (distance - first_hit) // size
            position = (position + distance) % size
        else:
            first_hit = position % size
            if first_hit == 0:
                first_hit = size
            if distance >= first_hit:
                hits += 1 + (distance - first_hit) // size
            position = (position - distance) % size
    return hits


def main() -> None:
    input_path = Path(__file__).with_name("input")
    raw = input_path.read_text().strip()
    rotations = parse_rotations(raw)
    part1 = count_zero_hits(rotations)
    part2 = count_zero_hits_per_click(rotations)
    print(part1)
    print(part2)


if __name__ == "__main__":
    main()
