import math
import random

MOVES = 0
SCORE = 0
def findMaxIndex(list):
    maximum = 0
    index = 0
    for element in range(len(list)):
        if list[element] > maximum:
            maximum = list[element]
            index = element

    return index

# Generates a random number if no parameter is given, if it is doesn't let that number to be picked again
def randomN(number = None):
    rnumber = random.randrange(0,6)
    while number != None and rnumber == number:
        rnumber = random.randrange(0,6)
        randomN(rnumber)
    return rnumber

# Generates a Matrix that is playable for the first move
def generateMatrix():
    MATRIX = []
    # Just creates a random matrix at first
    for everyRow in range(9):
        MATRIX.append([])
        for everyColumn in range(7):
            number = randomN()
            MATRIX[everyRow].append(number)

    # Checks if in every row there is a three in a row and changes to avoid that
    for eachRow in range(9):
        for eachColumn in range(2,7):
            if MATRIX[eachRow][eachColumn] == MATRIX[eachRow][eachColumn-1]:
                MATRIX[eachRow][eachColumn] = randomN(MATRIX[eachRow][eachColumn-1])

    # Checks if in every column there is a three in a row and changes to avoid that
    for iColumn in range(7):
        for iRow in range(2,9):
            if MATRIX[iRow][iColumn] == MATRIX[iRow-1][iColumn]:
                MATRIX[iRow][iColumn] = randomN(MATRIX[iRow-1][iColumn])

    # Returns the matrix
    return MATRIX

MATRIX = generateMatrix()

# Checks if the swap is adjacent and returns a boolean
def checkIfClickAdjacent(x,y,x1,y1):
    if x == x1-1 and y == y1:
        return True
    if x == x1+1 and y == y1:
        return True
    if y == y1+1 and x == x1:
        return True
    if y == y1-1 and x == x1:
        return True
    return False

# Swaps the user selection
def swap(x,y,x1,y1):
    temp = MATRIX[x1][y1]
    MATRIX[x1][y1] = MATRIX[x][y]
    MATRIX[x][y] = temp

# Checks that if swapping causes a match or not.
def checkIfThree():
    count = 0
    for everyRow in range(len(MATRIX)):
        for everyColumn in range(2,len(MATRIX[everyRow])):
            if MATRIX[everyRow][everyColumn] == MATRIX[everyRow][everyColumn-1] and MATRIX[everyRow][everyColumn] == MATRIX[everyRow][everyColumn-2]:
                count = 3

    for eachColumn in range(len(MATRIX[0])):
        for eachRow in range(2,len(MATRIX)):
            if MATRIX[eachRow][eachColumn] == MATRIX[eachRow-1][eachColumn] and MATRIX[eachRow][eachColumn] == MATRIX[eachRow-2][eachColumn]:
                count = 3

    if count == 3:
        similar()
        return True
    else:
        return False

# Removes a horizontal Match
def removeH(countH):
    global SCORE
    temp = 0
    index = 0
    for i in range(len(countH)):
        index = findMaxIndex(countH[i])
        if countH[i][index] >= 2:
            SCORE += (countH[i][index])+1
            temp = countH[i][index]
            for j in range(temp+1):
                MATRIX[i][index] = -1
                index -= 1

# Removes a Vertical Match
def removeV(countV):
    global SCORE
    temp = 0
    index = 0
    for i in range(len(countV)):
        index = findMaxIndex(countV[i])
        if countV[i][index] >= 2:
            SCORE += (countV[i][index])+1
            temp = (countV[i][index])
            for j in range(temp+1):
                MATRIX[index][i] = -1
                index -= 1


# Looks for a match
def similar():
    temp = 0
    countH = []
    for i in range(len(MATRIX)):
        countH.append([])
        for j in range(len(MATRIX[i])):
            if j != 0:
                if MATRIX[i][j] == MATRIX[i][j-1] and MATRIX[i][j] != -1:
                    temp += 1
                else:
                    temp = 0
            else:
                temp = 0
            countH[i].append(temp)
        temp = 0
    
    temp = 0
    countV = []
    for n in range(len(MATRIX[0])):
        countV.append([])
        for m in range(len(MATRIX)):
            if m != 0:
                if MATRIX[m][n] == MATRIX[m-1][n] and MATRIX[m][n] != -1:
                    temp += 1
                else:
                    temp = 0
            else:
                temp = 0
            countV[n].append(temp)
        temp = 0
    
    removeH(countH)
    removeV(countV)

def check1s():
    for eachRow in range(1,len(MATRIX)):
        for eachColumn in range(len(MATRIX[eachRow])):
            if MATRIX[eachRow][eachColumn] == -1:
                return True
    return False

def fillMatrix():
    temp = 0
    for eachRow in range(1,len(MATRIX)):
        for eachColumn in range(len(MATRIX[eachRow])):
            if MATRIX[eachRow][eachColumn] == -1:
                MATRIX[eachRow][eachColumn] = MATRIX[eachRow-1][eachColumn]
                MATRIX[eachRow-1][eachColumn] = -1


def fillRow0():
    for i in range(len(MATRIX[0])):
        if MATRIX[0][i] == -1:
            MATRIX[0][i] = randomN()



def checkVertical():
    print('This Ran')
    count = 0
    temp = 0
    for i in range(1,len(MATRIX[0])):
        if MATRIX[0][i] == -1:
            if MATRIX[1][i] == -1 and MATRIX[2][i] == -1:
                return False
    return True


def checkRow0():
    for i in range(len(MATRIX[0])):
        if MATRIX[0][i] == -1:
            return True
    return False


def fixMatrix():
    global SCORE
    while checkIfThree():
        similar()
        while check1s():
            fillMatrix()
            fillRow0()
    fillRow0()
    SCORE = 0 





