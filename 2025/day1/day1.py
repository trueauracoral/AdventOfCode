with open("input.txt", "r") as f:
    data = f.read().splitlines()

count = 50
zeroes = 0

def goLeft(value, count):
    for i, iteration in enumerate(list(range(value))):
        #iteration +=1
        count -= 1
        if (count < 0):
            count = 100 + count
    return count
def goRight(value, count):
    for i, iteration in enumerate(list(range(value))):
        #iteration +=1
        count += 1
        if (count > 99):
            count = count - 100
    return count

for line in data:
    direction = line[0]
    value = int(line[1:])
    if (direction == "L"):
        count = goLeft(value, count)
    elif (direction == "R"):
        count = goRight(value, count)

    print(f"The dial is rotated {line} to point at {count}")
    if (count == 0):
        zeroes += 1
print(count)
print(zeroes)

