with open("input.txt", "r") as f:
    data = f.read().splitlines()

def diagnostic(data):
    print(data)
    epigama = []
    binarySize = len(data[0])
    for i in range(binarySize):
        epigama.append({"0":0,"1":0})
    for line in data:
        line = list(line)
        for count, bit in enumerate(line):
            place = epigama[count]
            if bit == "0":
                place["0"] = place["0"] + 1
            if bit == "1":
                place["1"] = place["1"] + 1
    print(epigama)
    return epigama
def part1(data):
    epigama = diagnostic(data)
    gamma = ""
    epsilon = ""

    for bit in epigama:
        if bit["0"] > bit["1"]:
            gamma = gamma + "0"
            epsilon = epsilon + "1"
        if bit["0"] < bit["1"]:
            gamma = gamma + "1"
            epsilon = epsilon + "0"
    print(f"GAMMA: {gamma}")
    print(f"EPSILON: {epsilon}")
    print(int(gamma, 2) * int(epsilon, 2))

def part2(data):
    def valueToKey(epigama,value):
        return list(epigama.keys())[list(epigama.values()).index(value)]
    def filterNums(startValue):
        return [word for word in data if word.startswith(startValue)]
    epigama = diagnostic(data)

    def findOxygen(data):
        FILTER = ""
        count = 0
        while True:
            print(count)
            epigama = diagnostic(data)
            print(epigama)
            zeroes = epigama[count]['0']
            ones = epigama[count]['1']
            print(f"{count}: {zeroes} {ones}")
            if zeroes == ones:
                FILTER = FILTER + "1"
            else:
                FILTER = FILTER + valueToKey(epigama[count], max(zeroes,ones))
            print(FILTER)
            data = filterNums(FILTER)
            count = count + 1
            if (len(data) == 1):
                oxygen = data[0]
                return oxygen
                break
    def findC02(data):
        FILTER = ""
        count = 0
        while True:
            print(count)
            epigama = diagnostic(data)
            print(epigama)
            zeroes = epigama[count]['0']
            ones = epigama[count]['1']
            print(f"{count}: {zeroes} {ones}")
            if zeroes == ones:
                FILTER = FILTER + "0"
            else:
                FILTER = FILTER + valueToKey(epigama[count], min(zeroes,ones))
            print(FILTER)
            data = filterNums(FILTER)
            count = count + 1
            if (len(data) == 1):
                c02 = data[0]
                return c02
                break
    print(f"OXYGEN:\t{findOxygen(data)}")
    print(f"C02:\t{findC02(data)}")
    print(int(findOxygen(data), 2) * int(findC02(data), 2))

part1(data)
