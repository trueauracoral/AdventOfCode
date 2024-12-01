example = """3   4
4   3
2   5
1   3
3   9
3   3
"""
with open("input.txt", "r") as file:
    example = file.read()

firstList = []
secondList = []
for line in example.splitlines():
    line = line.split()
    firstNumber = line[0]
    secondNumber = line[1]
    firstList.append(firstNumber)
    secondList.append(secondNumber)
firstList.sort()
secondList.sort()

differenceList = []
for i, number in enumerate(firstList):
    firstNumber = int(firstList[i])
    secondNumber = int(secondList[i])
    difference = abs(firstNumber - secondNumber)
    differenceList.append(difference)

print(sum(differenceList))
