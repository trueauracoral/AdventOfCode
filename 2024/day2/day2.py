example = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9"""

with open("input.txt", "r") as f:
    example = f.read()

example = example.splitlines()
direction = None
totalGood = 0
def safeCheck(line):
    direction = None
    prev_level = int(line[0])
    for level in line[1:]:
        diff = int(level) - prev_level
        if diff == 0:
            return False
        elif diff < 0:
            if direction is None:
                direction = "decreasing"
            elif direction != "decreasing":
                return False
        else:
            if direction is None:
                direction = "increasing"
            elif direction != "increasing":
                return False
        if abs(diff) > 3:
            return False
        prev_level = int(level)
    return True

for line in example:
    line = line.split(" ")
    print(line)
    print(safeCheck(line))
    if (safeCheck(line)):
        totalGood+=1
    else:
        for i, number in enumerate(line):
            temp = line.copy()
            temp.pop(i)
            if (safeCheck(temp)):
                totalGood+=1
                break;

print(totalGood)
