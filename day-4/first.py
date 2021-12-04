with open("input.txt", "r") as f:
    markedNumbers = f.readline().replace(",", " ")
    bingoNumbers = f.readlines()

markedNumbers = [i for i in markedNumbers.split()]
bingoNumbers = [i.strip().split() for i in bingoNumbers]
bingoNumbers = [i for i in bingoNumbers if i != []]

winner = False

for marked in markedNumbers:
    for i in range(0, len(bingoNumbers)):
        for k in range(0, len(bingoNumbers[i])):
            if bingoNumbers[i][k] == marked:
                bingoNumbers[i][k] = 'X'
                if bingoNumbers[(i-1)//5][k] == 'X' and bingoNumbers[(i-1)//5 + 1][k] == 'X' and bingoNumbers[(i-1)//5 + 2][k] == 'X' and bingoNumbers[(i-1)//5 + 3][k] == 'X' and bingoNumbers[(i-1)//5 + 4][k] == 'X':
                    print(marked)
                    winner = True
                    break
                if bingoNumbers[i][k//5] == 'X' and bingoNumbers[i][k//5 + 1] == 'X' and bingoNumbers[i][k//5 + 2] == 'X' and bingoNumbers[i][k//5 + 3] == 'X' and bingoNumbers[i][k//5 + 4] == 'X':
                    print(marked)
                    winner = True
                    break
            if winner:
                break
        if winner:
            break
    if winner:
        break



