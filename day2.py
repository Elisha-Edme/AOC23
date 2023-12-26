import requests

sessionID="53616c7465645f5f28bc9c3bed317c1d97f3b2a74bb3d9f6bd782306dea6a640bc9f4c526729cc0f33494fb63b1e629013db8ce52a9bffa150eaaadaf5606e29"

inp = requests.get("https://adventofcode.com/2023/day/2/input", cookies={"session":sessionID}).text

def part1():
    cumSum = 0
    amounts = {"blue":14, "green":13, "red":12}
    for game in inp.split("\n"):
        # print(game)
        if len(game) > 1:
            ID = game[5:game.index(":")]
            possible = True
            for round in game[game.index(":") +1:].split(";"):
                round = round.strip()
                for marble in round.split(', '):
                    amount, color = marble.strip().split(' ')
                    # print(amount,color)
                    if amounts[color] < int(amount):
                        possible = False
            cumSum += (possible * int(ID))
    return cumSum

def part2():
    cumSum = 0
    for game in inp.split("\n"):
        # print(game)
        mins = {"blue":0, "green":0, "red":0}
        if len(game) > 1:
            for round in game[game.index(":") +1:].split(";"):
                round = round.strip()
                for marble in round.split(', '):
                    amount, color = marble.strip().split(' ')
                    mins[color] = max(mins[color], int(amount))
        mult = 1
        for val in list(mins.values()):
            mult *= val
        cumSum += mult
    return cumSum
print(part2())