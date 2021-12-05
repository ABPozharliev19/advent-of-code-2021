with open("input.txt", "r") as f:
    points = f.readlines()

points = [i.strip().split("->") for i in points]
points = [x.strip() for i in points for x in i]
points = [i.split(',') for i in points]
points = [int(x) for i in points for x in i]

print(points)

maximumX = points[0]
maximumY = points[0]

for i in range(0, len(points), 2):
    if points[i] > maximumX:
        maximumX = points[i]
    if points[i+1] > maximumY:
        maximumY = points[i+1]

pointSystem = [0] * ((maximumX + 1) * (maximumY + 1))

for i in range(0, len(points) - 3, 4):
    if points[i] != points[i+2] and points[i+1] != points[i+3]:
        # cases like 9,7 -> 7,9
        if points[i] > points[i+2] and (points[i] != points[i+1] and points[i+2] != points[i+3]):
            for k in range(0, (points[i] - points[i+2]) + 1):
                pointSystem[maximumX * (points[i + 2] + k) + (points[i + 3] - k)] = pointSystem[maximumX * (points[i + 2] + k) + (points[i + 3] - k)] + 1
        # cases like 5,5 -> 8,2
        elif points[i] < points[i+2] and (points[i] != points[i+1] and points[i+2] != points[i+3]):
            for k in range(0, (points[i+2] - points[i]) + 1):
                pointSystem[maximumX * (points[i + 2] - k) + (points[i + 3] + k)] = pointSystem[maximumX * (points[i + 2] - k) + (points[i + 3] + k)] + 1
        else:
            # cases like 1,1 -> 3,3
            if points[i] > points[i+2]:
                for k in range(0, (points[i] - points[i+2]) + 1):
                    pointSystem[maximumX * (points[i + 2] + k) + (points[i + 3] + k)] = pointSystem[maximumX * (points[i + 2] + k) + (points[i + 3] + k)] + 1
            # cases like 3,3 -> 1,1
            else:
                for k in range(0, (points[i+2] - points[i]) + 1):
                    pointSystem[maximumX * (points[i + 2] - k) + (points[i + 3] - k)] = pointSystem[maximumX * (points[i + 2] - k) + (points[i + 3] - k)] + 1

    else:
        if points[i] != points[i+2]:
            for k in range(min(points[i], points[i+2]), max(points[i], points[i+2]) + 1):
                pointSystem[maximumX * k + points[i+1]] = pointSystem[maximumX * k + points[i+1]] + 1
        else:
            for k in range(min(points[i+1], points[i + 3]), max(points[i+1], points[i + 3]) + 1):
                pointSystem[maximumX * points[i] + k] = pointSystem[maximumX * points[i] + k] + 1


overlappingPoints = 0

for y in range(0, maximumY):
    for x in range(0, maximumX):
        if pointSystem[x * maximumX + y] > 1:
            overlappingPoints = overlappingPoints + 1

print(overlappingPoints)
