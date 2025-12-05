from pathlib import Path


def max_two_digit_value(line: str) -> int:
    digits = [int(ch) for ch in line.strip()]
    if len(digits) < 2:
        raise ValueError("Line must contain at least 2 digits.")

    n = len(digits)
    suffix_max = [0] * n
    suffix_max[-1] = digits[-1]
    for i in range(n - 2, -1, -1):
        suffix_max[i] = max(digits[i], suffix_max[i + 1])

    best = -1
    for i in range(n - 1):
        candidate = digits[i] * 10 + suffix_max[i + 1]
        if candidate > best:
            best = candidate
    return best


def max_k_digit_value(line: str, k: int) -> int:
    digits = [int(ch) for ch in line.strip()]
    n = len(digits)
    if n < k:
        raise ValueError(f"Line must contain at least {k} digits.")

    to_remove = n - k
    stack: list[int] = []
    for d in digits:
        while to_remove and stack and stack[-1] < d:
            stack.pop()
            to_remove -= 1
        stack.append(d)

    if len(stack) > k:
        stack = stack[:k]

    value = 0
    for d in stack:
        value = value * 10 + d
    return value


def main() -> None:
    input_path = Path(__file__).with_name("input")
    lines = [line for line in input_path.read_text().strip().splitlines() if line.strip()]
    part1 = sum(max_two_digit_value(line) for line in lines)
    part2 = sum(max_k_digit_value(line, 12) for line in lines)
    print(part1)
    print(part2)


if __name__ == "__main__":
    main()
