import re

with open("src/year2023/day01/input.txt") as f:
    lines = f.read().strip().splitlines()


def parse1(line):
    digits = re.findall(r"\d", line)
    return int(digits[0] + digits[-1])


parsed1 = list(map(parse1, lines))
print("Part 1:", sum(parsed1))


def parse2(line):
    words = "one,two,three,four,five,six,seven,eight,nine".split(",")

    # positive lookahead to find `two` in `178ncllbfkkh4eightwoq`
    digits = re.findall(rf"(?=(\d|{'|'.join(words)}))", line)

    def to_digit(string):
        word_to_digit = dict(zip(words, range(1, 10)))
        return word_to_digit.get(string, string)  # default to digit

    return int(f"{to_digit(digits[0])}{to_digit(digits[-1])}")


print("Part 2:", sum(map(parse2, lines)))
