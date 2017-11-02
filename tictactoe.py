#Gary Li
#11/1/17
#tictactoe.py

square1
square2
square3
square4
square5
square6
square7
square8
square9

def printBoard():
    for i in range(1,4):
        print('+---'*3+'+')
        print('|   '*3+'|')
    print('+---'*3+'+')

def isEmpty(numSquare):
    if 'X' in numSquare or 'O' in numSquare:
        return False
    return True

printBoard()
