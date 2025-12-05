from bisect import bisect_right
from pathlib import Path


def parse_database(raw: str) -> tuple[list[tuple[int, int]], list[int]]:
    upper, lower = raw.strip().split("\n\n", 1)
    ranges: list[tuple[int, int]] = []
    for line in upper.splitlines():
        if not line.strip():
            continue
        start, end = line.split("-")
        ranges.append((int(start), int(end)))
    ids = [int(line) for line in lower.splitlines() if line.strip()]
    return ranges, ids


def merge_ranges(ranges: list[tuple[int, int]]) -> list[tuple[int, int]]:
    if not ranges:
        return []
    ranges.sort()
    merged: list[tuple[int, int]] = []
    cur_start, cur_end = ranges[0]
    for start, end in ranges[1:]:
        if start <= cur_end + 1:
            cur_end = max(cur_end, end)
        else:
            merged.append((cur_start, cur_end))
            cur_start, cur_end = start, end
    merged.append((cur_start, cur_end))
    return merged


def count_fresh(ranges: list[tuple[int, int]], ids: list[int]) -> int:
    merged = merge_ranges(ranges)
    starts = [s for s, _ in merged]
    total = 0
    for val in ids:
        idx = bisect_right(starts, val) - 1
        if idx >= 0:
            _, end = merged[idx]
            if val <= end:
                total += 1
    return total


def count_fresh_coverage(ranges: list[tuple[int, int]]) -> int:
    merged = merge_ranges(ranges)
    return sum(end - start + 1 for start, end in merged)


def main() -> None:
    input_path = Path(__file__).with_name("input")
    raw = input_path.read_text()
    ranges, ids = parse_database(raw)
    part1 = count_fresh(ranges, ids)
    part2 = count_fresh_coverage(ranges)
    print(part1)
    print(part2)


if __name__ == "__main__":
    main()
