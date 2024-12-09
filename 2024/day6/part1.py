example ="""....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#..."""

with open("input.txt", "r") as f:
    example = f.read()

example = example.splitlines()
for index, value in enumerate(example):
    if "^" in value:
        subindex = value.index("^")
        break
grid = []
for line in example:
    line = list(line)
    grid.append(line)

print(grid)
x,y=subindex,index
print(x)
print(y)

def printGrid():
    for line in grid:
        line = ''.join(line)
        print(line)

turnRight = {
    "up": "right",
    "right": "down",
    "down": "left",
    "left": "up"
}
direction = "up"
count = 0
def isValid(x, y):
    if (x >= 0 and x < len(grid[0]) and y>=0 and y<len(grid)):
        return True
    else:
        return False

def isCrate(x,y):
    if grid[y][x] == "#":
        return True
    else:
        return False


def moveInDirection(x, y):
    if (direction == "up"):
        y-=1
    elif (direction == "down"):
        y+=1
    elif (direction == "left"):
        x-=1
    elif (direction == "right"):
        x+=1
    return [x, y]

while True:
    #grid[y][x] = '.'
    newCoords = moveInDirection(x, y)
    print(newCoords)
    if isValid(newCoords[0], newCoords[1]):
        if isCrate(newCoords[0], newCoords[1]):
            direction = turnRight[direction]
            #count+=1
        else:
            y = newCoords[1]
            x = newCoords[0]
            grid[y][x] = '^'
    else:
        break
    print(count)
    printGrid()

for line in grid:
    for char in line:
        if char == "^":
            count+=1

print(count)
