import requests

sessionID="53616c7465645f5f28bc9c3bed317c1d97f3b2a74bb3d9f6bd782306dea6a640bc9f4c526729cc0f33494fb63b1e629013db8ce52a9bffa150eaaadaf5606e29"

inp = requests.get("https://adventofcode.com/2023/day/3/input", cookies={"session":sessionID}).text

def part1():
    lst = inp.split("\n")
    indices = []
    for row in lst:
        for char in row:
            pass
print(part1())