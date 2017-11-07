#Gary Li
#11/1/17
#tictactoe.py

square1 = 1
square2 = 2
square3 = 3
square4 = 4
square5 = 5
square6 = 6
square7 = 7
square8 = 8
square9 = 9

def printBoard():
    print('_____________')
    print('|', square1, '|', square2, '|',square3, '|')
    print('_____________')
    print('|', square4, '|', square5, '|',square6, '|')
    print('_____________')
    print('|', square7, '|', square8, '|',square9, '|')
    print('_____________')

def isEmpty(squareChosen):
    if 'X' in square1 or 'O' in square1:
        return False
    else:
        return True
    if 'X' in square2 or 'O' in square2:
        return False
    else:
        return True
    if 'X' in square3 or 'O' in square3:
        return False
    else:
        return True
    if 'X' in square4 or 'O' in square4:
        return False
    else:
        return True
    if 'X' in square5 or 'O' in square5:
        return False
    else:
        return True
    if 'X' in square6 or 'O' in square6:
        return False
    else:
        return True
    if 'X' in square7 or 'O' in square7:
        return False
    else:
        return True
    if 'X' in square8 or 'O' in square8:
        return False
    else:
        return True
    if 'X' in square9 or 'O' in square9:
        return False
    else:
        return True

def fullBoard(squareChosen):
    if square1 == 'X' or square1 == 'O':
        if square2 == 'X' or square2 == 'O':
            if square3 == 'X' or square3 == 'O':
                if square4 == 'X' or square4 == 'O':
                    if square5 == 'X' or square5 == 'O':
                        if square6 == 'X' or square6 == 'O':
                            if square7 == 'X' or square7 == 'O':
                                if square8 == 'X' or square8 == 'O':
                                    if square9 == 'X' or square9 == 'O':
                                        return True
    else: return False

if __name__ == '__main__':
    while True:
        printBoard()
        squareChosen=(int(input('Where would you like to go?')))
        while isEmpty(squareChosen) == False:
            print('Try another square')
            squareChosen=(int(input('Where would you like to go?')))
        if squareChosen == 1:
            square1 = 'X'
        if squareChosen == 2:
            square2 = 'X'
        if squareChosen == 3:
            square3 = 'X'
        if squareChosen == 4:
            square4 = 'X'
        if squareChosen == 5:
            square5 = 'X'
        if squareChosen == 6:
            square6 = 'X'
        if squareChosen == 7:
            square7 = 'X'
        if squareChosen == 8:
            square8 = 'X'
        if squareChosen == 9:
            square9 = 'X'
        if fullBoard(squareChosen) is True:
            break
        