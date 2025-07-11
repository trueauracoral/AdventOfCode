def convertToInts(data):
    data = data.splitlines()[:-1]
    data = [int(x) for x in data]
    return data

sample = """199
200
208
210
200
207
240
269
260
263

"""
sample = convertToInts(sample)
with open("input.txt", "r") as f:
    inputData = f.read()
inputData = convertToInts(inputData)

def part1(sample):
    answer = 0
    for count, value in enumerate(sample[1:]):
        count = count + 1
        print(f"COUNT: {count}")
        print()
        print(sample[count-1])
        print(value)
        if int(value) > int(sample[count-1]):
            print("GREATER")
            answer = answer + 1
    print(f"ANSWER: {answer}")
    return answer

def part2(data):
    print(data)
    previouses = []
    for count, value in enumerate(data):
        previous = 0
        print(f"VALUE: {value}")
        for i in range(3):
            if count + i < len(data):
                print(f"ACESS INT: {count + i}")
                print(f"FOUND:     {data[count+i]}")
                print(f"LOOP:      {i}")
                previous = previous + data[count +i]
        print(previous)
        print()
        previouses.append(previous)
    previouses = previouses[:-2]
    print(previouses)
    return previouses
print(sample)

print("\n\n")

print(part1(part2(inputData)))
#part1(inputData)
