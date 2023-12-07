import re
from functools import reduce

from utils import *

with open("src/year2023/day06/input.txt") as f:
    lines = f.read().splitlines()


def extract(string):
    return re.findall(r"\d+", string)


def distance(t_held, t_total):
    return t_held * (t_total - t_held)


def ways_to_win(race):
    race_time, race_record = race
    for t_held in range(0, race_time + 1):
        if distance(t_held, race_time) > race_record:
            yield t_held


races = zip(
    map(int, extract(lines[0])),
    map(int, extract(lines[1])),
)
ways = list(map(list, map(ways_to_win, races)))
print("Part 1:", reduce(lambda x, y: x * y, map(len, ways)))


race = (
    int("".join(extract(lines[0]))),
    int("".join(extract(lines[1]))),
)
ways = list(ways_to_win(race))  # 5.647 seconds
print("Part 2:", len(ways))
