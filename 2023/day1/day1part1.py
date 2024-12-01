
with open("input.txt", "r") as f:
    data = f.read().splitlines()

def calibrate(data):
    total = 0
    matches = []
    for i, line in enumerate(data):
        match = []
        for number in list(line):
            if number.isdigit():
                match.append(number)
        matches.append(match)
        if len(match) != 0:
            first = match[0]
            second = match[-1]
            calibration = int(str(first) + str(second))
            total = total + calibration
    print(total)

calibrate(data)
