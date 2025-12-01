with open("sample.txt", "r") as f:
    data = list(map(int,f.read().replace("\n","").split(",")))

print(data)
def part2():
    positions = []
    fuel = 0
    for position in range(max(data))[1:]:
        for i in range(len(data)):
            difference = abs(data[i]-position)+1
            fuel += (difference * (difference - 1))/2
            #fuel += sum(list(range(difference)))
            #print(f"Move from {data[i]} to {position}: fuel:{sum(list(range(difference)))}")

        positions.append(fuel)
        fuel = 0
        print(position)
    print(min(positions))

def part1():
    positions = []
    fuel = 0
    for position in range(2000)[1:]:
        for i in range(len(data)):
            fuel += abs(data[i]-position)
        positions.append(fuel)
        print(f"Pos:{position}, fuel:{fuel}")
        fuel = 0
    print(min(positions))
part2()
