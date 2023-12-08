from collections import Counter

with open("src/year2023/day07/input.txt") as f:
    lines = f.read().splitlines()


def parse_line(string):
    t = string.split(" ")
    return {"cards": t[0], "bid": int(t[1])}


alpha = "abcdefghijklmnopqrstuvwxyz"


def card_strength1(card):
    return alpha["AKQJT98765432".index(card)]


def card_strength2(card):
    return alpha["AKQT98765432J".index(card)]


def type_strength1(hand):
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


def type_strength2(hand):
    hand = hand["cards"]
    print(hand, end=" -> ")

    if hand == "JJJJJ":
        hand = "AAAAA"
    elif "J" in hand:
        sansj = hand.replace("J", "")

        def sortkey(c):
            return str(4 - Counter(sansj).get(c)) + card_strength2(c)

        replacement = sorted(sansj, key=sortkey)[0]
        # print(candidates, end=" ")
        hand = hand.replace("J", replacement)
    print(hand)

    counts = Counter(hand)
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


def strength1(hand):
    card_strengths = map(card_strength1, hand["cards"])
    return str(type_strength1(hand)) + "".join(card_strengths)


def strength2(hand):
    card_strengths = map(card_strength2, hand["cards"])
    return str(type_strength2(hand)) + "".join(card_strengths)


def score(ranked):
    for rank, hand in ranked:
        yield rank * hand["bid"]


hands = list(map(parse_line, lines))

ranked = enumerate(sorted(hands, key=strength1, reverse=True), start=1)
print("Part 1:", sum(score(ranked)))

ranked = enumerate(sorted(hands, key=strength2, reverse=True), start=1)
print("Part 2:", sum(score(ranked)))
