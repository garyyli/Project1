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

def isEmpty(numSquare):
    if 'X' in numSquare or 'O' in numSquare:
        return False
    else:
        return True
    
        
        
    isEmpty(int(input('Where would you like to go?')))
    printBoard()
