import re

with open("src/year2023/day04/input.txt") as f:
    lines = f.read().splitlines()


def parse_sequence(string):
    return set(map(int, re.findall(r"\d+", string)))


def parse_card(line):
    wins, your = map(parse_sequence, line.split(":")[1].split("|"))
    return wins & your


def score1(numbers):
    return 2 ** (len(numbers) - 1) if numbers else 0


card_winners = list(map(parse_card, lines))
print("Part 1:", sum(map(score1, card_winners)))


def playthrough2(winners):
    origs = dict(enumerate(map(len, winners), start=1))  # {1: 4, 2: 2, ...}
    q = list(origs.keys())
    while q:
        card = q.pop()
        q.extend(range(card + 1, card + origs[card] + 1))
        yield card


cards_played = list(playthrough2(card_winners))
print("Part 2:", len(cards_played))
