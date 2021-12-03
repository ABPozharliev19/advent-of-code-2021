with open("input.txt", "r") as f:
    inputData = f.readlines()

inputData = [i.strip() for i in inputData]

oxygenGenerator = inputData.copy()

index = 0

sumOfBits = 0
lastBit = ""
removedBits = 0

# Getting the oxygen number first
while len(oxygenGenerator) - removedBits > 1:
    for number in oxygenGenerator:
        # If the number hasn't been marked as removed yet
        if number == "U":
            continue
        sumOfBits = sumOfBits + (1 if number[index] == "1" else -1)

    if sumOfBits == 0:
        lastBit = "1"
    else:
        lastBit = "1" if sumOfBits > 0 else "0"

    for ind in range(0, len(oxygenGenerator)):
        if oxygenGenerator[ind] != "U":
            if oxygenGenerator[ind][index] != lastBit:
                # Mark the removed numbers with "U"
                oxygenGenerator[ind] = "U"
                removedBits = removedBits + 1

    index = index + 1
    sumOfBits = 0

print(oxygenGenerator)

# Getting the CO2 number

removedBits = 0
index = 0
removedBits = 0

coGenerator = inputData.copy()

while len(coGenerator) - removedBits > 1:
    for number in coGenerator:
        if number == "U":
            continue
        sumOfBits = sumOfBits + (1 if number[index] == "1" else -1)

    if sumOfBits == 0:
        lastBit = "0"
    else:
        lastBit = "0" if sumOfBits > 0 else "1"

    for ind in range(0, len(coGenerator)):
        if coGenerator[ind] != "U":
            if coGenerator[ind][index] != lastBit:
                coGenerator[ind] = "U"
                removedBits = removedBits + 1
    index = index + 1
    sumOfBits = 0

print(coGenerator)





