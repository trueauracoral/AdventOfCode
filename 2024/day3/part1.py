import re

#example = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
#example = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
with open("input.txt", "r") as f:
    example = f.read()

regexResults = re.findall("mul\((\d+)\,+(\d+)\)", example)

total = 0
indexList = []
for result in regexResults:
    result = list(result)
    indexer = f"mul({result[0]},{result[1]})"
    indexList.append({'index': example.find(indexer), 'value': result})
    for i, value in enumerate(result):
        result[i] = value

    total += int(result[0]) * int(result[1])
print("TOTAL:" + str(total))
