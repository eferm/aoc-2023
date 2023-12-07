import argparse
import os
import pathlib
from datetime import date

import requests
from dotenv import load_dotenv

load_dotenv(verbose=True)

SESSION = os.getenv("SESSION")

TEMPLATE = """from utils import *

with open("{folder}/input.txt") as f:
    lines = f.read().splitlines()

lprint(lines[:10])
"""


def get_input(year, day):
    url = f"https://adventofcode.com/{year}/day/{day}/input"
    headers = {
        "Cookie": f"session={SESSION}",
    }

    print(f"Fetching input for {year=} {day=} from server...")
    resp = requests.get(url, headers=headers)
    resp.raise_for_status()

    return resp.text


def bootstrap():
    parser = argparse.ArgumentParser(description=__doc__)

    parser.add_argument("day", type=int)
    parser.add_argument("-y", "--year", type=int, default=date.today().year)

    args = parser.parse_args()

    folder = pathlib.Path("src", f"year{args.year}", f"day{args.day:02}")
    folder.mkdir(exist_ok=True)

    if not (f := folder / "main.py").exists():
        print(f"Seeding file {f}...")
        f.write_text(TEMPLATE.format(folder=folder))

    if not (f := folder / "input.txt").exists():
        print(f"Seeding file {f}...")
        f.write_text(get_input(args.year, args.day))

    folder.joinpath("example1.txt").touch()
    folder.joinpath("example2.txt").touch()
