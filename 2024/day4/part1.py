import re
example = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX"""

with open("input.txt", "r") as f:
    example = f.read()

#example = """.M.S......
#..A..MSMS.
#.M.S.MAA..
#..A.ASMSM.
#.M.S.M....
#..........
#S.S.S.S.S.
#.A.A.A.A..
#M.M.M.M.M.
#.........."""

grid = []
for line in example.splitlines():
    line = list(line)
    grid.append(line)
print(grid)

def horizontalSearch(example):
    xmas = len(re.findall("XMAS", example))
    samx = len(re.findall("SAMX", example))
    return xmas + samx

def verticalSearch(example, search):
    firstchar = search[0]
    count = 0
    for row, line in enumerate(example.splitlines()):
        line = list(line)
        for col, character in enumerate(line):
            if (grid[row][col] == firstchar):
                wordfound = []
                for num in range(4):
                    try:
                        wordfound.append(grid[row+num][col])
                    except:
                        break
                wordfound = ''.join(wordfound)
                if (wordfound == search):
                    count+=1
    return count

def diagonalSearch(example, search):
    print(search)
    firstchar = search[0]
    count = 0
    for row, line in enumerate(example.splitlines()):
        line = list(line)
        for col, character in enumerate(line):
            if (grid[row][col] == firstchar):
                wordfound = []
                for num in range(4):
                    if (col+num >= len(line) or row+num >= len(line)):
                        break
                    else:
                        #print(f"row: {row+num}, col: {col+num}")
                        wordfound.append(grid[row+num][col+num])
                wordfound = ''.join(wordfound)
                if (wordfound == search):
                    #print(f"{wordfound} | {search}")
                    count+=1
            if (grid[row][col] == firstchar):
                wordfound = []
                for num in range(4):
                    if (col-num >= 0 and col-num < len(line) and row+num < len(grid) and row+num >= 0):
                        print(f"row: {row+num}, col: {col-num}")
                        wordfound.append(grid[row+num][col-num])
                    else:
                        break
                #print()
                wordfound = ''.join(wordfound)
                #print(wordfound)
                if (wordfound == search):
                    #print(f"{wordfound} | {search}")
                    count+=1
    return count

#horizontal = horizontalSearch(example)
#print(f"Horizontal: {horizontal}")
#vertical = verticalSearch(example, "XMAS") + verticalSearch(example, "SAMX")
#print(f"Vertical: {vertical}")
#diagonal = diagonalSearch(example, "XMAS") + diagonalSearch(example, "SAMX")
#print(diagonal + horizontal + vertical)

def MASSearch(example, search):
    firstchar = search[0]
    count = 0
    for row, line in enumerate(grid):
        for col, character in enumerate(line):
            if (character == firstchar):
                wordfound = []
                for num in range(3):
                    if (
                        row + num < len(grid)
                        and col + num < len(grid[0])
                    ):
                        wordfound.append(grid[row+num][col+num])
                    else :
                        break
                wordfound = ''.join(wordfound)
                if (wordfound == search):
                    #print(f"{wordfound} | {search}")
                    wordfound = []
                    for num in range(3):
                        newcol=col+2
                        if (newcol-num >= 0 and newcol-num < len(grid) and row+num < len(grid[0]) and row+num >= 0):
                            print(f"row: {row+num}, col: {newcol-num}")
                            print(grid[row+num][newcol-num])
                            wordfound.append(grid[row+num][newcol-num])
                        else :
                            break
                    print(wordfound)
                    wordfound = ''.join(wordfound)
                    if (wordfound == search):
                        #print(f"{wordfound} | {search}")
                        count+=1
                    elif (search == "MAS"):
                        if (wordfound == "SAM"):
                            count+=1
                    elif (search == "SAM"):
                        if (wordfound == "MAS"):
                            count+=1
                    print(count)
    return count

totalMAS = MASSearch(example, "MAS") + MASSearch(example, "SAM")

print(totalMAS)
