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

def isEmpty():
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
isEmpty(int(input('Where would you like to go?')))

printBoard()
