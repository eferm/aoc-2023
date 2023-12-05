import re
from collections import defaultdict
from functools import reduce

with open("src/year2023/day03/input.txt") as f:
    inp = f.read().strip()

print(inp)

WIDTH = len(inp.splitlines()[0]) + 1  # incl newline
HEIGHT = len(inp.splitlines())

print(WIDTH, "width", "x", HEIGHT, "height")


def indexes(pattern, string):
    for m in re.finditer(pattern, string):
        yield m.start(), m.end() - 1


def trim(target_row, start, end):
    return (
        min(max(start, target_row * WIDTH, 0), HEIGHT * WIDTH),
        max(min(end, target_row * WIDTH + WIDTH, HEIGHT * WIDTH), 0),
    )


def adj_positions(start, end):
    row = start // WIDTH
    u = trim(row - 1, start - WIDTH - 1, end - WIDTH + 1)
    d = trim(row + 1, start + WIDTH - 1, end + WIDTH + 1)
    l = trim(row, start - 1, start - 1)
    r = trim(row, end + 1, end + 1)
    return [u, d, l, r]


def valid1(inp):
    for start, end in indexes(r"\d+", inp):
        neighbors = [inp[i : j + 1] for i, j in adj_positions(start, end)]
        is_part_number = re.findall(r"[^\.\d\n]", "".join(neighbors))
        # print(f"{start // WIDTH:03} {inp[start : end + 1]:03}", is_part_number)
        if is_part_number:
            yield int(inp[start : end + 1])


print("Part 1:", sum(valid1(inp)))


def adj_positions(start, end, inp):
    row = start // WIDTH
    u = trim(row - 1, start - WIDTH - 1, end - WIDTH + 1)
    d = trim(row + 1, start + WIDTH - 1, end + WIDTH + 1)
    l = trim(row, start - 1, start - 1)
    r = trim(row, end + 1, end + 1)
    for start, end in [u, d, l, r]:
        yield start, end, inp[start : end + 1]


def valid2(inp):
    gears = defaultdict(list)
    for start, end in indexes(r"\d+", inp):
        for i, _, symbols in adj_positions(start, end, inp):
            if "*" in symbols:
                for j, _ in indexes(r"[*]", symbols):
                    gears[i + j].append(int(inp[start : end + 1]))
    for k, v in gears.items():
        if len(v) > 1:
            yield reduce(lambda x, y: x * y, v, 1)


print("Part 2:", sum(valid2(inp)))
