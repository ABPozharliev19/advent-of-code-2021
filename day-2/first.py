with open("input.txt", "r") as f:
    inputData = f.readlines()

inputData = [i.strip().split() for i in inputData]

depth = 0
horizontal = 0

for i in inputData:
    if i[0] == 'forward':
        horizontal = horizontal + int(i[1])
    elif i[0] == 'down':
        depth = depth + int(i[1])
    else:
        depth = depth - int(i[1])

print(depth * horizontal)