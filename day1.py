import requests
sessionID="53616c7465645f5f28bc9c3bed317c1d97f3b2a74bb3d9f6bd782306dea6a640bc9f4c526729cc0f33494fb63b1e629013db8ce52a9bffa150eaaadaf5606e29"

inp = requests.get("https://adventofcode.com/2023/day/1/input", cookies={"session":sessionID}).text

def partOne():
    getAllNums = lambda x: [(i, int(x[i])) for i in range(len(x)) if x[i].isdigit()]
    cumSum = 0
    for line in inp.split():
        nums = getAllNums(line)
        if len(nums) > 0:
            number = nums[0] *10 + nums[-1]
            cumSum += number
    return cumSum

def part2():
    words = ["one", "two", "three", 'four', 'five', 'six', 'seven', 'eight', 'nine']
    convert = lambda x: x if type(x) == int else (words.index(x) + 1)
    cumSum = 0
    for line in inp.split():
        if len(line) > 0:
            firsts, lasts = [], []
            for word, number in zip(words, [i for i in range(1,10)]):
                firsts.append((line.index(word) if word in line else len(line), word))
                firsts.append((line.index(str(number)) if str(number) in line else len(line), number))
                lasts.append((line.rfind(word), word))
                lasts.append((line.rfind(str(number)), number))
            number = convert(min(firsts, key=lambda x: x[0])[1], ) * 10 + convert(max(lasts, key=lambda x: x[0])[1])
            cumSum += number
    return cumSum
print(part2())


        
