import re

from utils import *

with open("src/year2023/day09/input.txt") as f:
    lines = f.read().splitlines()


def parse_sequence(line):
    return list(map(int, re.findall(r"-?\d+", line)))


def pairwise_diffs(seq):
    return [seq[i + 1] - seq[i] for i in range(0, len(seq) - 1)]


def recurse(seq):
    # print(seq)
    if len(set(diffs := pairwise_diffs(seq))) == 1:
        # print(diffs)
        return seq + [seq[-1] + diffs.pop()]
    return seq + [seq[-1] + recurse(pairwise_diffs(seq))[-1]]


values = list(map(parse_sequence, lines))
# lprint(values)
# print("")


predicted = [v[-1] for v in map(recurse, values)]
# lprint(predicted)
print("Part 1:", sum(predicted))
