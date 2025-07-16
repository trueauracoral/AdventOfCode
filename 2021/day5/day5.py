with open("sample.txt", "r") as f:
    Data = f.read().splitlines()
def getCol(matrix, i):
    return [row[i] for row in matrix]
def printMatrix(matrix):
    for row in matrix:
        for item in row:
            if item == 0:
                print(".",end='')
            else:
                print(item, end='')
        print()

data = []
for count, line in enumerate(Data):
    line = line.replace(" -> ", ",")
    line = line.split(",")
    data.append(list(map(int, line)))
print(data)

width = max(max(getCol(data,0)), max(getCol(data,2)))
height = max(max(getCol(data,1)), max(getCol(data,3)))

diagram = []
for row in range(height+1):
    roweth = []
    for col in range(width+1):
        roweth.append(0)
    diagram.append(roweth)
print(diagram)

def part1():
    for line in data:
        x1 = line[0]
        x2 = line[2]
        y1 = line[1]
        y2 = line[3]
        print(f"x1:{x1},y1:{y1},x2:{x2},y2:{y2}")
        if (x1==x2):
            for coord in list(range(min(y1,y2), max(y1,y2)+1)):
                print(f"x:{coord},y:{y1}")
                diagram[coord][x1] += 1
        if (y1==y2):
            for coord in range(min(x1,x2),max(x1,x2)+1):
                print(f"x:{x1},y:{coord}")
                diagram[y1][coord] += 1

    printMatrix(diagram)
    SUM = 0
    for row in diagram:
        for item in row:
            if item >=2:
                SUM+=1
    print(SUM)

def part2():
    for line in data:
        x1 = line[0]
        x2 = line[2]
        y1 = line[1]
        y2 = line[3]
        print(f"x1:{x1},y1:{y1},x2:{x2},y2:{y2}")
        if abs(x1-x2) == abs(y1-y2):
            xVal = -1
            if (x2 > x1):
                xVal = 1
            yVal = -1
            if (y2 > y1):
                yVal = 1

            for i in range(abs(x1 - x2) + 1):
                x = x1 + i * xVal
                y = y1 + i * yVal
                print(f"x:{x},y:{y}")
                diagram[y][x] += 1
        elif (x1==x2):
            for coord in list(range(min(y1,y2), max(y1,y2)+1)):
                print(f"x:{coord},y:{y1}")
                diagram[coord][x1] += 1
        elif (y1==y2):
            for coord in range(min(x1,x2),max(x1,x2)+1):
                print(f"x:{x1},y:{coord}")
                diagram[y1][coord] += 1

    printMatrix(diagram)
    SUM = 0
    for row in diagram:
        for item in row:
            if item >=2:
                SUM+=1
    print(SUM)

if (__name__ == '__main__'):
    part2()
#part1()
