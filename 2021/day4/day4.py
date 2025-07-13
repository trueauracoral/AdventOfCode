with open("input.txt", "r") as f:
    data = f.read().splitlines()

numbers = data[0].split(",")
boards = []
for i in range(int(len(data[1:]) / 6)):
    board = []
    for line in range(5):
        board.append(data[i*6 + line + 2].split())
    boards.append(board)
print()

print(numbers)
def getColumn(matrix, i):
    return [row[i] for row in matrix]
def part1():
    for number in numbers:
        for count, board in enumerate(boards):
            markedBoard = []
            for rowi, row in enumerate(board):
                for coli, item in enumerate(row):
                    if int(item.replace("m","")) == int(number):
                        print(f"BOARD: {count}, ROW: {rowi}, COL: {coli}")
                        print(f"Number: {number} - boardNum: {item}")
                        board[rowi][coli] = board[rowi][coli] + "m"
            markedBoard = board
            print()
            print(markedBoard)
            for count, row in enumerate(markedBoard):
                row = ''.join(row)
                col = ''.join(getColumn(markedBoard,count))
                print(row)
                print(row.count("m"))
                print(col)
                if (row.count("m") == 5 or col.count("m") == 5):
                    SUM = 0
                    for row in markedBoard:
                        for item in row:
                            if "m" not in item:
                                SUM += int(item)
                    print(SUM)
                    print(number)
                    return SUM * int(number)

def part2():
    answers ={}
    for number in numbers:
        for count, board in enumerate(boards):
            markedBoard = []
            for rowi, row in enumerate(board):
                for coli, item in enumerate(row):
                    if int(item.replace("m","")) == int(number):
                        print(f"BOARD: {count}, ROW: {rowi}, COL: {coli}")
                        print(f"Number: {number} - boardNum: {item}")
                        board[rowi][coli] = board[rowi][coli] + "m"
            markedBoard = board
            print()
            print(markedBoard)
            for cow, row in enumerate(markedBoard):
                row = ''.join(row)
                col = ''.join(getColumn(markedBoard,cow))
                print(row)
                print(row.count("m"))
                print(col)
                if (row.count("m") == 5 or col.count("m") == 5):
                    SUM = 0
                    for row in markedBoard:
                        for item in row:
                            if "m" not in item:
                                SUM += int(item)
                    print(SUM)
                    print(number)
                    answer = SUM * int(number)
                    if answer != 0 and count not in answers:
                        answers[count] = answer
                        break
    return answers[list(answers)[-1]]

print(part2())
#print(part1())
