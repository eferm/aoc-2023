import itertools

from utils import *

with open("src/year2023/day11/input.txt") as f:
    image = f.read().splitlines()

# lprint(image)


ROWS = len(image)
COLS = len(image[0])
print(f"{ROWS}x{COLS}")


def empty(seq):
    return set(seq) == {"."}


def column(mat, c):
    return "".join([row[c] for row in mat])


def transposed(mat):
    mat = list(mat)
    for c in range(len(mat[0])):
        yield column(mat, c)


def expanded(mat):
    for row in mat:
        yield row
        if empty(row):
            yield "." * len(row)


def get_galaxies(mat):
    for r, row in enumerate(mat):
        for c, val in enumerate(row):
            if val == "#":
                yield (r, c)


def distance(a, b):
    return abs(b[0] - a[0]) + abs(b[1] - a[1])


def distances(galaxies):
    for a, b in itertools.combinations(range(len(galaxies)), 2):
        ga, gb = galaxies[a], galaxies[b]
        # print(a + 1, "->", b + 1, end=": ")
        yield distance(ga, gb)


expanded = transposed(expanded(transposed(expanded(image))))
galaxies = dict(enumerate(get_galaxies(expanded)))
print("Part 1", sum(distances(galaxies)))
