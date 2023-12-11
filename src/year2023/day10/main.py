from collections import namedtuple

from utils import *

with open("src/year2023/day10/input.txt") as f:
    lines = f.read().splitlines()

WIDTH = len(lines[0])
HEIGHT = len(lines)

# lprint(lines)
# print(f"{WIDTH}x{HEIGHT}")
# print("")

map_ = []

C = "."
map_ += [C * (WIDTH + 2)]
for l in lines:
    map_ += [C + l + C]
map_ += [C * (WIDTH + 2)]

print("framed")
lprint(map_)
print("")


def find_start(map_, symbol="S"):
    for r, row in enumerate(map_):
        for c, val in enumerate(row):
            if val == symbol:
                return coord(r, c)


coord = namedtuple("coord", ["r", "c"])

# for vector _key_, _values_ are valid symbols in that direction
valids = {
    coord(-1, 0): ["|", "7", "F"],  # look north
    coord(1, 0): ["|", "J", "L"],  # look south
    coord(0, -1): ["-", "L", "F"],  # look west
    coord(0, 1): ["-", "J", "7"],  # look east
}

# if on symbol _key_, then _values_ are valid vectors I can move to
orient = {
    ",": [coord(-1, 0), coord(1, 0), coord(0, -1), coord(0, 1)],
    ".": [coord(-1, 0), coord(1, 0), coord(0, -1), coord(0, 1)],
    "S": [coord(-1, 0), coord(1, 0), coord(0, -1), coord(0, 1)],
    "|": [coord(-1, 0), coord(1, 0)],
    "-": [coord(0, -1), coord(0, 1)],
    "L": [coord(-1, 0), coord(0, 1)],
    "J": [coord(-1, 0), coord(0, -1)],
    "7": [coord(1, 0), coord(0, -1)],
    "F": [coord(1, 0), coord(0, 1)],
}


def get_neighbors(map_, curr, filter_contiguous_pipe=True):
    symbol = map_[curr.r][curr.c]
    for delta in orient[symbol]:
        neighbor = coord(curr.r + delta.r, curr.c + delta.c)
        if 0 < neighbor.r < len(map_) and 0 < neighbor.c < len(map_[0]):
            if filter_contiguous_pipe:
                if map_[neighbor.r][neighbor.c] in valids[delta]:
                    yield neighbor
            else:
                yield neighbor


seen = []
curr = find_start(map_, "S")

while curr not in seen:
    seen.append(curr)
    for neighbor in get_neighbors(map_, curr):
        if neighbor not in seen:
            curr = neighbor

# print("Part 1:", len(seen) // 2)


def mask(map_, coords, char=" "):
    for r, row in enumerate(map_):
        yield "".join(
            val if coord(r, c) in coords else char for c, val in enumerate(row)
        )


map_ = list(mask(map_, seen, char="."))
print("simplified")
lprint(map_)


def sparse_right(map_):
    newmap = []
    for r, row in enumerate(map_):
        newrow = ""
        for i in range(0, len(row)):
            if row[i] == ".":
                newrow += ",."  # shift right
            elif row[i] in ["|", "J", "7"]:
                newrow += row[i] + ","
            elif row[i] in ["-", "F", "L"]:
                newrow += row[i] + "-"
            elif row[i] == "S":
                if row[i + 1] in ["-", "J", "7"]:
                    newrow += "S-"
                else:
                    newrow += "S."
            elif row[i] == "*":
                if i == 0 or i == len(row) - 1:
                    newrow += "*"
                else:
                    newrow += "**"
        newmap.append(newrow)
    return newmap


def sparse_down(map_):
    newmap = []
    for r in range(0, len(map_)):
        thisrow = ""
        nextrow = ""
        for c, val in enumerate(map_[r]):
            if val == ".":
                thisrow += ","
                nextrow += "."  # shift
            elif val in ["|", "F", "7"]:
                thisrow += val
                nextrow += "|"
            elif val in ["-", "L", "J"]:
                thisrow += val
                nextrow += ","
            elif val == "S":
                if map_[r + 1][c] in ["|", "J", "L"]:
                    thisrow += "S"
                    nextrow += "|"
                else:
                    thisrow += "S"
                    nextrow += ","
            elif val == ",":
                thisrow += ","
                nextrow += ","
            # elif val == "*":
            #     if r == 0:
            #         nextrow += "*"
            #     elif r == len(map_) - 1:
            #         thisrow += "*"
            #     elif c == 0 or c == len(map_[r]) - 1:
            #         thisrow += "*"
            #         nextrow += "*"

        if thisrow:
            newmap.append(thisrow)
        if nextrow:
            newmap.append(nextrow)
    return newmap


map_sparse = list(sparse_right(map_))
# lprint(map_sparse)
map_sparse = list(sparse_down(map_sparse))
print("sparse")
lprint(map_sparse)


def get_connected(map_, node, seen):
    symbol = map_[node.r][node.c]
    q = [node]
    while q:
        n = q.pop(0)
        if n not in seen and map_[n.r][n.c] in [symbol, ","]:
            seen.append(n)
            yield n
            q.extend(get_neighbors(map_, n, False))


def get_clusters(map_):
    seen = []
    for r in range(0, len(map_)):
        for c in range(0, len(map_[0])):
            if coord(r, c) not in seen and map_[r][c] in [".", ","]:
                yield list(get_connected(map_, coord(r, c), seen))


cluster = next(get_clusters(map_sparse))
# print("cluster")
# lprint(mask(map_sparse, cluster))

map_inner = []
count = 0
dots = []
for r, row in enumerate(map_sparse):
    newrow = ""
    for c, val in enumerate(row):
        newrow += " " if coord(r, c) in cluster else val
        if val == ".":
            dots.append(coord(r, c))

    print(newrow)
    count += newrow.count(".")
    map_inner.append(newrow)

lprint(mask(map_inner, dots))
print(count)
# lprint(map_inner)


# # for cluster in clusters:
# #     lprint(mask(map_, cluster))

# # print(clusters)


# # print(map_sparse[2][2])


# def surrounded(map_, node):
#     sides = []
#     for delta, valid in {
#         coord(-1, 0): ["-"],
#         coord(1, 0): ["-"],
#         coord(0, -1): ["|"],
#         coord(0, 1): ["|"],
#     }.items():
#         curr = node
#         while map_[curr.r][curr.c] in [".", " "]:
#             if not (0 < curr.r < HEIGHT + 2 and 0 < curr.c < WIDTH + 2):
#                 break
#             curr = coord(curr.r + delta.r, curr.c + delta.c)
#         sides.append(map_[curr.r][curr.c] in valid)
#     return all(sides)


# def offset(node):
#     return coord(2 * node.r, 2 * node.c)


# contained = []
# for cluster in clusters:
#     # lprint(mask(map_, cluster))
#     # print(cluster)
#     sides = list(
#         map(lambda n: surrounded(map_sparse, n), map(offset, cluster))
#     )
#     # print(sides)
#     if all(sides):
#         # print("surrounded")
#         contained.extend(cluster)

# lprint(mask(map_, clusters[0]))
# lprint(mask(map_, contained))
# print("Part 2:", len(contained))
# # 597 too high

# # print([len(l) for i, l in enumerate(clusters) if contained[i]])
# # contained = map(lambda n: surrounded(map_sparse, n), sparse_offset(cluster))
# # for cluster in clusters:

# #     print(
# #         list(map(lambda n: surrounded(map_sparse, n), sparse_offset(cluster)))
# #     )


# # print(clusters[0])
# # lprint(mask(map_sparse, list(sparse_offset(clusters[1]))))
# # seen = []
# # clusters = []


# # for r, c in zip(range(0, WIDTH), range(0, HEIGHT)):
# #     curr = coord(r, c)
# #     if curr not in seen:
# #         seen.append(curr)
# #         if map_[curr.r][curr.c] == ".":
# #             cluster = [curr]
# #             neighbors = get_neighbors(map_, curr, filter_contiguous_pipe=False)
# #             q = [n for n in neighbors if map_[n.r][n.c] == "."]
# #             while q:
# #                 dot = q.pop(0)
# #                 if dot not in seen:
# #                     seen.append(dot)
# #                     cluster.append(dot)
# #                     neighbors = get_neighbors(
# #                         map_, dot, filter_contiguous_pipe=False
# #                     )
# #                     q.extend([n for n in neighbors if map_[n.r][n.c] == "."])
# #             clusters.append(cluster)

# # print(clusters)

# # seen = []
# # curr = coord(0, 0)

# # while curr not in seen:
# #     seen.append(curr)
# #     q = []
# #     for neighbor in get_neighbors(map_, curr):
# #         if neighbor not in seen and map_[neighbor.r][neighbor.c] == ".":
# #             q.append(neighbor)

# #             curr = neighbor


# # #         if row[i] == ""
# # # "S": [coord(-1, 0), coord(1, 0), coord(0, -1), coord(0, 1)],
# # # "|": [coord(-1, 0), coord(1, 0)],
# # # "-": [coord(0, -1), coord(0, 1)],
# # # "L": [coord(-1, 0), coord(0, 1)],
# # # "J": [coord(-1, 0), coord(0, -1)],
# # # "7": [coord(1, 0), coord(0, -1)],
# # # "F": [coord(1, 0), coord(0, 1)],


# # # lprint(mask(map_, seen))


# # # | is a vertical pipe connecting north and south.
# # # - is a horizontal pipe connecting east and west.
# # # L is a 90-degree bend connecting north and east.
# # # J is a 90-degree bend connecting north and west.
# # # 7 is a 90-degree bend connecting south and west.
# # # F is a 90-degree bend connecting south and east.
# # # . is ground; there is no pipe in this tile.
# # # S is the starting position of the animal; there is a pipe on this tile, but your sketch doesn't show what shape the pipe has.

# # # orient = {
# # #     ""
# # # }

# # # # lines.insert(HEIGHT, "." * (WIDTH + 2))
# # # # lines.insert(0, "." * (WIDTH + 2))
# # # # for
# # # # lprint(lines)
# # # # lprint(lines)
