with open("input.txt", "r") as f:
    inputData = f.readlines()

inputData = [i.strip() for i in inputData]

index = 0

gamma = ""
epsilon = ""

sumOfBits = 0

while index < 12:
    for number in inputData:
        sumOfBits = sumOfBits + (1 if number[index] == "1" else -1)

    if sumOfBits > 0:
        gamma = gamma + "1"
        epsilon = epsilon + "0"
    else:
        gamma = gamma + "0"
        epsilon = epsilon + "1"
    sumOfBits = 0
    index = index + 1

print(gamma)
print(epsilon)