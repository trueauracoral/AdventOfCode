with open("input.txt", "r") as f:
    data = f.read().splitlines()
with open("example", "r") as f:
    example = f.read().splitlines()

numberToInt = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9
}
def calibrate(data):
    sum = 0
    inputs = list(numberToInt.keys())
    matches = []
    for line in data:
        match = []
        for number in inputs:
            if number in line:
                match.append(numberToInt[number])
        matches.append(match)
    for match in matches:
        if len(match) != 0:
            first = match[0]
            second = match[-1]
            sum = sum + int(str(first) + str(second))
    print(sum)

calibrate(data)
