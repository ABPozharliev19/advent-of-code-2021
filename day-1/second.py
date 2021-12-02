with open("input.txt", "r") as f:
    daysInfo = f.readlines()

counter = 0

for i in range(0, len(daysInfo) - 3):
    nextThreeDays = int(daysInfo[i].strip()) + int(daysInfo[i+1].strip()) + int(daysInfo[i+2].strip())
    nextThreeDaysPlusOne = int(daysInfo[i+1].strip()) + int(daysInfo[i+2].strip()) + int(daysInfo[i+3].strip())
    if nextThreeDays < nextThreeDaysPlusOne:
        counter = counter + 1

print(counter)
