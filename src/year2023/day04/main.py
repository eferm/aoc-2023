import re

with open("src/year2023/day04/input.txt") as f:
    lines = f.read().splitlines()


def parse_sequence(string):
    return set(map(int, re.findall(r"\d+", string)))


def parse_card(line):
    wins, your = map(parse_sequence, line.split(":")[1].split("|"))
    winning = wins & your
    return 2 ** (len(winning) - 1) if len(winning) else 0


print("Part 1:", sum(map(parse_card, lines)))
