from collections import Counter

with open("src/year2023/day07/input.txt") as f:
    lines = f.read().splitlines()


def parse_line(string):
    t = string.split(" ")
    return {"cards": t[0], "bid": int(t[1])}


def card_strength(card):
    return "AKQJT98765432".index(card)


def type_strength(hand):
    counts = Counter(hand["cards"])
    if max(counts.values()) == 5:
        return 0
    if max(counts.values()) == 4:
        return 1
    if counts.most_common()[0][1] == 3 and counts.most_common()[1][1] == 2:
        return 2
    if max(counts.values()) == 3:
        return 3
    if counts.most_common()[0][1] == 2 and counts.most_common()[1][1] == 2:
        return 4
    if max(counts.values()) == 2:
        return 5
    return 6


def strength(hand):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    card_strengths = map(card_strength, hand["cards"])
    card_strengths_str = map(lambda i: alpha[i], card_strengths)  # make 1 char
    return str(type_strength(hand)) + "".join(card_strengths_str)


def score(hands):
    ranked = enumerate(sorted(hands, key=strength, reverse=True), start=1)
    for rank, hand in ranked:
        yield rank * hand["bid"]


hands = map(parse_line, lines)
print("Part 1:", sum(score(hands)))
