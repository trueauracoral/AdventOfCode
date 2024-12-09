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

example = example.splitlines()
for i, line in enumerate(example):
    if len(line) == 0:
        part1 = example[:i]
        part2 = example[i+1:]
        break

part2 = '\n'.join(part2)

correctList = []
def searchOrder(pages):
    for line in part1:
        line = line.split("|")
        search = re.findall(f"{line[0]}\,(.+)\,{line[1]}", pages)
        print(search)
        if len(search) != 0:
            if (len(search[0].split(",")) == 1 and len(search) != 0):
                correctList.append(search[0])
            #elif (len(search[0].split(",")) == 3):
            #    searchOrder(search[0])

searchOrder(part2)
print(correctList)
