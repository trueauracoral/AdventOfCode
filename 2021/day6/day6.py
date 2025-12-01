from collections import defaultdict

with open("input.txt", "r") as f:
    data = list(map(int, f.read().replace("\n","").split(",")))

print(data)
Data = defaultdict(int)
for i in data:
    Data[int(i)] += 1
def day2(Data):
    for day in range(256):
        dataDict = defaultdict(int)
        for key in Data:
            if key == 0:
                dataDict[6] += Data[key]
                dataDict[8] =  Data[key]
            else:
                dataDict[key - 1] += Data[key]
        print(dataDict)
        Data = dataDict
    print(dataDict)
    answer = 0
    for key in dataDict:
        answer += dataDict[key]
    print(answer)

    #print(len(data))

def day1():
    print(data)
    def simulate():
        for i in range(len(data)):
            data[i] -= 1
            if data[i] == -1:
                data[i] = 6
                data.append(8)
        return data
    for count, i in enumerate(range(256)):
        simulate()
        #print(f"After {count+1} days: {data}")
        #print(len(data))
        print(count)
    print(len(data))

day2(Data)
