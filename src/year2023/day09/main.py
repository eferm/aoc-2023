import re

from utils import *

with open("src/year2023/day09/input.txt") as f:
    lines = f.read().splitlines()


def parse_sequence(line):
    return list(map(int, re.findall(r"-?\d+", line)))


def pairwise_diffs(seq):
    return [seq[i + 1] - seq[i] for i in range(0, len(seq) - 1)]


def recurse1(seq):
    # print(seq)
    if len(set(diffs := pairwise_diffs(seq))) == 1:
        # print(diffs)
        return seq + [seq[-1] + diffs.pop()]
    return seq + [seq[-1] + recurse1(pairwise_diffs(seq))[-1]]


def recurse2(seq):
    # print(seq)
    if len(set(diffs := pairwise_diffs(seq))) == 1:
        # print(diffs)
        return [seq[0] - diffs.pop()] + seq
    return [seq[0] - recurse2(pairwise_diffs(seq))[0]] + seq


values = list(map(parse_sequence, lines))
# lprint(values)
# print("")


predicted1 = [v[-1] for v in map(recurse1, values)]
print("Part 1:", sum(predicted1))

predicted2 = [v[0] for v in map(recurse2, values)]
print("Part 2:", sum(predicted2))
