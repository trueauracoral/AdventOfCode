from collections import deque

with open("sample.txt", "r") as f:
    data = list(map(int, f.read().replace("\n","").split(",")))

print(data)
def day2(data):
    print(data)
    def simulate(result):
        for i in range(len(result)):
            result[i] -= 1
            countChildren = 0
            if result[i] == -1:
                result[i] = 6
                countChildren += 1
            result = result + [8] * countChildren
        return result
    for count, i in enumerate(range(256)):
        data = simulate(data)
        #print(f"After {count+1} days: {data}")
        #print(len(data))
        print(count)
    print(len(data))

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

day2(data)
