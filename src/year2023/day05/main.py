import re
from collections import namedtuple

from utils import *

with open("src/year2023/day05/input.txt") as f:
    chunks = f.read().strip().split("\n\n")


def parse_numbers(string):
    return lmap(int, re.findall(r"\d+", string))


def parse_map(chunk):
    # -> [[50, 98, 2], ...]
    numbers = map(parse_numbers, chunk.splitlines()[1:])
    # -> [seedmap(dst=50, src=98, len=2), ...]
    return list(map(namedtuple("map_", ["dst", "src", "len"])._make, numbers))


def lookup(map_, val):
    for r in map_:
        # for m in sorted(maps, key=lambda m: m.src, reverse=True):
        if r.src <= val < r.src + r.len:
            return r.dst + (val - r.src)
    return val


def locations(maps, seeds):
    for s in seeds:
        # print(s, end=" ")
        t = s
        for m in maps:
            t = lookup(m, t)
            # print(t, end=" ")
        yield t


seeds = list(parse_numbers(chunks[0]))
# print(seeds)

# lprint(chunks[1:])
maps = lmap(parse_map, chunks[1:])
# print(maps)

# print(lookup(maps[0], 13))

# 79 81 81 81 74 78 78 82
# 14 14 53 49 42 42 43 43

locs = list(locations(maps, seeds))
print("Part 1:", min(locs))
