sample = """forward 5
down 5
forward 8
up 3
down 8
forward 2
"""
sample = sample.splitlines()

with open("input.txt", "r") as f:
    inputData = f.read().splitlines()[:-1]

def part1(data):
    horizontal = 0
    depth = 0
    for line in data:
        line = line.split(" ")
        print(line)
        direction = line[0]
        amount = int(line[1])
        match direction:
            case "forward":
                horizontal = horizontal + amount
            case "down":
                depth = depth + amount
            case "up":
                depth = depth - amount
            case _:
                return "Uh oh..."
    return horizontal * depth

def part2(data):
    horizontal = 0
    depth = 0
    aim = 0
    for line in data:
        line = line.split(" ")
        print(line)
        direction = line[0]
        amount = int(line[1])
        match direction:
            case "forward":
                horizontal = horizontal + amount
                depth = depth + (aim * amount)
            case "down":
                aim = aim + amount
            case "up":
                aim = aim - amount
            case _:
                return "Uh oh..."
    return horizontal * depth

print(part2(inputData))
#print(part1(inputData))
