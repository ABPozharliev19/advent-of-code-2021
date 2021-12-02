with open("input.txt", 'r') as f:
    daysInfo = f.readlines()

counter = 0

for i in range(0, len(daysInfo) - 1):
    if int(daysInfo[i].strip()) < int(daysInfo[i+1].strip()):
        counter = counter + 1

print(counter)
