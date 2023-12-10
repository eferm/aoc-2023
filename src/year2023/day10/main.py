from collections import namedtuple

from utils import *

with open("src/year2023/day10/input.txt") as f:
    lines = f.read().splitlines()

WIDTH = len(lines[0])
HEIGHT = len(lines)

lprint(lines)
# print(f"{WIDTH}x{HEIGHT}")
print("")

map_ = []

map_ += ["." * (WIDTH + 2)]
for l in lines:
    map_ += [f".{l}."]
map_ += ["." * (WIDTH + 2)]

lprint(map_)
print("")


def find_start(map_, symbol="S"):
    for r, row in enumerate(map_):
        for c, val in enumerate(row):
            if val == symbol:
                return coord(r, c)


coord = namedtuple("coord", ["r", "c"])

orient = {
    "S": {
        coord(-1, 0): ["|", "7", "F"],  # look north
        coord(1, 0): ["|", "J", "L"],  # look south
        coord(0, -1): ["-", "L", "F"],  # look west
        coord(0, 1): ["-", "J", "7"],  # look east
    },
    "|": {
        coord(-1, 0): ["|", "7", "F"],  # look north
        coord(1, 0): ["|", "J", "L"],  # look south
        coord(0, -1): [],  # look west
        coord(0, 1): [],  # look east
    },
    "-": {
        coord(-1, 0): [],  # look north
        coord(1, 0): [],  # look south
        coord(0, -1): ["-", "L", "F"],  # look west
        coord(0, 1): ["-", "J", "7"],  # look east
    },
    "L": {
        coord(-1, 0): ["|", "7", "F"],  # look north
        coord(1, 0): [],  # look south
        coord(0, -1): [],  # look west
        coord(0, 1): ["-", "J", "7"],  # look east
    },
    "J": {
        coord(-1, 0): ["|", "7", "F"],  # look north
        coord(1, 0): [],  # look south
        coord(0, -1): ["-", "L", "F"],  # look west
        coord(0, 1): [],  # look east
    },
    "7": {
        coord(-1, 0): [],  # look north
        coord(1, 0): ["|", "J", "L"],  # look south
        coord(0, -1): ["-", "L", "F"],  # look west
        coord(0, 1): [],  # look east
    },
    "F": {
        coord(-1, 0): [],  # look north
        coord(1, 0): ["|", "J", "L"],  # look south
        coord(0, -1): [],  # look west
        coord(0, 1): ["-", "J", "7"],  # look east
    },
}


def get_neighbors(map_, curr):
    symbol = map_[curr.r][curr.c]
    valids = orient[symbol]

    for delta, valid in valids.items():
        neighbor = coord(curr.r + delta.r, curr.c + delta.c)
        if map_[neighbor.r][neighbor.c] in valid:
            yield neighbor


print(map_[2][2])
start = find_start(map_, "S")
print(start)

seen = []
curr = find_start(map_, "S")

while curr not in seen:
    seen.append(curr)
    for neighbor in get_neighbors(map_, curr):
        if neighbor not in seen:
            curr = neighbor

print(seen)
print(len(seen) // 2)


# def mask(map_, coords):
#     for r, row in enumerate(map_):
#         yield "".join(
#             val if coord(r, c) in coords else "." for c, val in enumerate(row)
#         )


# lprint(mask(map_, seen))


# | is a vertical pipe connecting north and south.
# - is a horizontal pipe connecting east and west.
# L is a 90-degree bend connecting north and east.
# J is a 90-degree bend connecting north and west.
# 7 is a 90-degree bend connecting south and west.
# F is a 90-degree bend connecting south and east.
# . is ground; there is no pipe in this tile.
# S is the starting position of the animal; there is a pipe on this tile, but your sketch doesn't show what shape the pipe has.

# orient = {
#     ""
# }

# # lines.insert(HEIGHT, "." * (WIDTH + 2))
# # lines.insert(0, "." * (WIDTH + 2))
# # for
# # lprint(lines)
# # lprint(lines)
