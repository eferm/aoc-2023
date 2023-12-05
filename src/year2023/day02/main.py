import re
from collections import defaultdict
from functools import reduce

filename = "input.txt"
with open("src/year2023/day02/" + filename) as f:
    lines = f.read().strip().splitlines()


def parse_observation(string):
    """Transform '3 blue' -> {"blue": 3}"""
    t = string.split(" ")
    return {t[1]: int(t[0])}


def parse_game_round(string):
    """Transform '3 blue, 4 red' -> {"blue": 3, "red": 4}"""
    dicts = map(parse_observation, string.split(", "))
    return dict(t for d in dicts for t in d.items())  # flatten


def parse_game(line):
    string = re.match(r"^Game \d+: (.*)", line).group(1)

    # -> [{"blue": 3, "red": 4}, {"blue": 2}]
    game_rounds = map(parse_game_round, string.split("; "))

    # -> {"blue": [3, 2], "red": [4]}
    summary = defaultdict(list)
    for game_round in game_rounds:
        for k, v in game_round.items():
            summary[k].append(v)

    return summary


def valid1(games, thresh):
    for i, game in enumerate(games):
        if all(max(game[k]) <= thresh[k] for k in game):
            yield i + 1


games = list(map(parse_game, lines))

valids = valid1(games, {"red": 12, "green": 13, "blue": 14})
print("Part 1:", sum(valids))


def valid2(games):
    for game in games:
        maxes = [max(v) for _, v in game.items()]
        yield reduce(lambda x, y: x * y, maxes, 1)


print("Part 2:", sum(valid2(games)))
