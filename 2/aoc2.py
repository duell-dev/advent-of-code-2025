from pathlib import Path


def parse_ranges(raw: str) -> list[tuple[int, int]]:
    cleaned = raw.replace("\n", "")
    ranges: list[tuple[int, int]] = []
    for part in cleaned.split(","):
        part = part.strip()
        if not part:
            continue
        start_str, end_str = part.split("-")
        ranges.append((int(start_str), int(end_str)))
    return ranges


def generate_repeated_numbers(max_value: int) -> list[int]:
    repeated: list[int] = []
    max_digits = len(str(max_value))
    for block_len in range(1, max_digits + 1):
        base_start = 10 ** (block_len - 1)
        base_end = 10**block_len - 1
        for block in range(base_start, base_end + 1):
            s = str(block)
            repeated_str = s + s 
            while len(repeated_str) <= max_digits:
                num = int(repeated_str)
                if num > max_value:
                    break
                repeated.append(num)
                repeated_str += s 
            if int(str(base_start) * 2) > max_value:
                break
    return sorted(set(repeated))


def main() -> None:
    input_path = Path(__file__).with_name("input")
    raw = input_path.read_text()
    ranges = parse_ranges(raw)
    max_value = max(end for _, end in ranges)

    repeated_numbers = generate_repeated_numbers(max_value)
    events: list[tuple[int, int]] = []
    for idx, (start, end) in enumerate(ranges):
        events.append((start, idx))
        events.append((end + 1, ~idx))
    events.sort()

    total = 0
    active = 0
    ev_idx = 0
    n_ranges = len(ranges)
    weights = [0] * n_ranges
    for num in repeated_numbers:
        while ev_idx < len(events) and events[ev_idx][0] <= num:
            pos, marker = events[ev_idx]
            if marker >= 0:
                active += 1
            else:
                active -= 1
            ev_idx += 1
        total += num * active

    print(total)


if __name__ == "__main__":
    main()
