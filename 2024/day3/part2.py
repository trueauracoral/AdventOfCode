import re

with open("input.txt", "r") as f:
    example = f.read()
#previous = indexList[0]
#safe = False
#total = int(indexList[0]['value'][0]) * int(indexList[0]['value'][1])
#for result in indexList[1:]:
#    newer = result
#    #print(f"{previous['index']} | {newer['index']}")
#    donot = example.find("don't()", previous['index'], newer['index'])
#    dosafe = example.find("do()", previous['index'], newer['index'])
#    #print(f"do(): {dosafe}")
#    #print(f"donot(): {donot}")
#    if (donot != -1 and donot > dosafe):
#        safe = False
#    elif (dosafe != -1 and dosafe > donot):
#        safe = True
#    #print(safe)
#    if (safe):
#        total+= int(result['value'][0]) * int(result['value'][1])
#    previous = result
#print(total)

regexResults = re.findall("mul\((\d+)\,+(\d+)\)|(do\(\))|(don't\(\)+)", example)
total = 0
indexList = []
safe = True
for result in regexResults:
    result = list(filter(lambda x: x != "", list(result)))
    if len(result) == 1:
        result = result[0]
        if (result == "do()"):
            safe = True
            continue
        elif (result == "don't()"):
            safe = False
            continue
    if (safe):
        try:
            total += int(result[0]) * int(result[1])
        except:
            print(result)
            break;
print("TOTAL: " + str(total))

