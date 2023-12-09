import itertools
import re

from utils import *

with open("src/year2023/day08/input.txt") as f:
    chunks = f.read().split("\n\n")


def parse_mapping(string):
    nodes = re.findall(r"[A-Z]+", string)
    return {nodes[0]: {"L": nodes[1], "R": nodes[2]}}


def parse_nodes(string):
    return {
        k: v
        for i in map(parse_mapping, string.splitlines())
        for k, v in i.items()
    }


def navigate(instructions, nodes):
    curr = "AAA"
    for instr in itertools.cycle(instructions):
        if curr == "ZZZ":
            return
        yield curr
        curr = nodes[curr][instr]


instructions = chunks[0]
nodes = parse_nodes(chunks[1])
# print(nodes)
print(len(list(navigate(instructions, nodes))))
