import functools
import itertools
import math
import re

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


def navigate(instr, nodes, ends, start):
    curr = start
    for i in itertools.cycle(instr):
        if curr in ends:
            return curr
        yield 1
        curr = nodes[curr][i]


instr = chunks[0]
nodes = parse_nodes(chunks[1])

navigate1 = functools.partial(navigate, instr, nodes, ["ZZZ"])
print("Part 1:", sum(navigate1("AAA")))


starting = [k for k in nodes if k.endswith("A")]
ending = [k for k in nodes if k.endswith("Z")]
navigate2 = functools.partial(navigate, instr, nodes, ending)
print("Part 2:", math.lcm(*map(sum, map(navigate2, starting))))
