def solve(data: list, days: int):
    for t in range(days):
        for i in range(0, len(data)):
            if data[i] == 0:
                data[i] = 6
                data.append(8)
                continue
            data[i] = data[i] - 1


with open("input.txt", "r") as f:
    inputData = f.readlines()

inputData = [i.split(',') for i in inputData]

# Un-nests the list
cleaned = [int(val) for sublist in inputData for val in sublist]

print(solve(cleaned, 80))
print(solve(cleaned, 256))
