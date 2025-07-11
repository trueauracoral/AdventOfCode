import re

example = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47"""

with open("input.txt", "r") as f:
    example = f.read()

example = example.splitlines()
for i, line in enumerate(example):
    if len(line) == 0:
        part1 = example[:i]
        part2 = example[i+1:]
        break

#part2 = '\n'.join(part2)

leftRules = []
rightRules = []

for rule in part1:
    rule = rule.split("|")
    leftRules.append(rule[0])
    rightRules.append(rule[1])

print(part2)
validList = []
for update in part2:
    update = update.split(",")
    for page in update:
        rules = [i for i, x in enumerate(leftRules) if x == page]
        for i, rule in enumerate(rules):
            leftValue = leftRules[rule]
            rightValue = rightRules[rule]
            print(f"{leftValue}|{rightValue}")
            distance = 0
            if leftValue in update:
                leftValueIndex = update.index(leftValue)
                if rightValue in update:
                    rightValueIndex = update.index(rightValue)
                    print(f"distance {rightValueIndex} - {leftValueIndex}: {rightValueIndex-leftValueIndex}")
                    distance = rightValueIndex - leftValueIndex
                    if distance < 0:
                        break
                else:
                    print(f"is completed: {i} - {len(rules)- 1}")
                    if (i+1 < len(rules) -1):
                        print("HELLO I CONTINUED")
                        continue
                    else:
                        break
            else:
                break
        if (distance > 0):
            if update not in validList:
                validList.append(update)
print(validList)
result = 0
for valid in validList:
    middle = int(valid[int((len(valid) - 1) / 2)])
    result+=middle

print(result)
