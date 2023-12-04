import re

with open("src/year2023/day01/input.txt") as f:
    inp = f.read().strip().split()


def parse1(line):
    first = re.match(r"^.*?(\d)", line).group(1)
    last = re.match(r".*(\d).*$", line).groups()[-1]
    return int(f"{first}{last}")


parsed1 = list(map(parse1, inp))
print("part 1:", sum(parsed1))


words = [
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
]


def parse2(line):
    first = re.match(rf"^.*?(\d|{'|'.join(words)})", line).group(1)
    last = re.match(rf".*(\d|{'|'.join(words)}).*$", line).groups()[-1]

    to_digit = dict(zip(words, range(1, 10)))
    return int(f"{to_digit.get(first, first)}{to_digit.get(last, last)}")


parsed2 = list(map(parse2, inp))
print("part 2:", sum(parsed2))
