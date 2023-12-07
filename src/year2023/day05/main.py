import re
from collections import namedtuple

with open("src/year2023/day05/input.txt") as f:
    chunks = f.read().strip().split("\n\n")


map_ = namedtuple("map_", ["dst", "src", "len"])
range_ = namedtuple("range_", ["src", "len"])


def parse_numbers(string):
    return list(map(int, re.findall(r"\d+", string)))


def parse_map(chunk):
    # -> [[50, 98, 2], ...]
    numbers = map(parse_numbers, chunk.splitlines()[1:])
    # -> [map_(dst=50, src=98, len=2), ...]
    return list(map(map_._make, numbers))


def lookup(map_, val):
    for m in map_:
        if m.src <= val < m.src + m.len:
            return m.dst + (val - m.src)
    return val


def lookup_range(map_, val):
    src_min = val.src
    for m in sorted(map_, key=lambda x: x.src):
        if m.src <= src_min <= m.src + m.len:
            src_max = min(val.src + val.len, m.src + m.len)
            offset = src_min - m.src
            length = src_max - src_min
            yield range_(m.dst + offset, length)
            # continue if didn't map entire src range
            if src_max < val.src + val.len:
                src_min = src_max
            else:
                break
    # return self if didn't find map for src range
    else:
        yield val


def locations(maps, seeds):
    for s in seeds:
        t = s
        for m in maps:
            t = lookup(m, t)
        yield t


def location_ranges(maps, seeds):
    for seed, length in zip(
        [seeds[i] for i in range(0, len(seeds), 2)],
        [seeds[i] for i in range(1, len(seeds), 2)],
    ):
        q = [range_(seed, length)]
        for m in maps:
            next_q = []
            while q:
                r = q.pop(0)
                next_q.extend(list(lookup_range(m, r)))
            q = next_q
        yield q


maps = list(map(parse_map, chunks[1:]))
seeds = parse_numbers(chunks[0])

locs = list(locations(maps, seeds))
print("Part 1:", min(locs))

locs = list(location_ranges(maps, seeds))
print("Part 2:", min(min(locs)).src)
