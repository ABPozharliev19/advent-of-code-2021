with open("input.txt", "r") as f:
    inputData = f.readlines()

inputData = [i.strip().split() for i in inputData]

depth = 0
horizontal = 0
aim = 0

for i in inputData:
    if i[0] == 'forward':
        horizontal = horizontal + int(i[1])
        depth = depth + aim * int(i[1])
    elif i[0] == 'down':
        aim = aim + int(i[1])
    else:
        aim = aim - int(i[1])

print(depth * horizontal)