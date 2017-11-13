#Gary Li
#11/1/17
#tictactoe.py

from random import randint

square1 = 1
square2 = 2
square3 = 3
square4 = 4
square5 = 5
square6 = 6
square7 = 7
square8 = 8
square9 = 9

def printBoard(): #prints out the board
    print('_____________')
    print('|', square1, '|', square2, '|',square3, '|')
    print('_____________')
    print('|', square4, '|', square5, '|',square6, '|')
    print('_____________')
    print('|', square7, '|', square8, '|',square9, '|')
    print('_____________')

def isEmpty(squareChosen): #determines whether or not a square is empty for the player to make a move in
    if squareChosen == 1:
        if square1 == 'X' or square1 == 'O':
            return False
        else:
            return True
    elif squareChosen == 2:
        if square2 == 'X' or square2 == 'O':
            return False
        else:
            return True
    elif squareChosen == 3:
        if square3 == 'X' or square3 == 'O':
            return False
        else:
            return True
    elif squareChosen == 4:
        if square4 == 'X' or square4 == 'O':
            return False
        else:
            return True
    elif squareChosen == 5:
        if square5 == 'X' or square5 == 'O':
            return False
        else:
            return True
    elif squareChosen == 6:
        if square6 == 'X' or square6 == 'O':
            return False
        else:
            return True
    elif squareChosen == 7:
        if square7 == 'X' or square7 == 'O':
            return False
        else:
            return True
    elif squareChosen == 8:
        if square8 == 'X' or square8 == 'O':
            return False
        else:
            return True
    elif squareChosen == 9:
        if square9 == 'X' or square9 == 'O':
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

def winner():
    if square1 == 'X' and square2 == 'X' and square3 == 'X':
        return True
    elif square1 == 'O' and square2 == 'O' and square3 == 'O':
        return True
    elif square4 == 'X' and square5 == 'X' and square6 == 'X':
        return True
    elif square4 == 'O' and square5 == 'O' and square6 == 'O':
        return True
    elif square7 == 'X' and square8 == 'X' and square9 == 'X':
        return True
    elif square7 == 'O' and square8 == 'O' and square9 == 'O':
        return True
    elif square1 == 'X' and square4 == 'X' and square7 == 'X':
        return True
    elif square1 == 'O' and square4 == 'O' and square7 == 'O':
        return True
    elif square2 == 'X' and square5 == 'X' and square8 == 'X':
        return True
    elif square2 == 'O' and square5 == 'O' and square8 == 'O':
        return True
    elif square3 == 'X' and square6 == 'X' and square9 == 'X':
        return True
    elif square3 == 'O' and square6 == 'O' and square9 == 'O':
        return True
    elif square1 == 'X' and square5 == 'X' and square9 == 'X':
        return True
    elif square1 == 'O' and square5 == 'O' and square9 == 'O':
        return True
    elif square3 == 'X' and square5 == 'X' and square7 == 'X':
        return True
    elif square3 == 'O' and square5 == 'O' and square7 == 'O':
        return True
    else:
        return False

if __name__ == '__main__':
    while True:
        printBoard()
        squareChosen=(int(input('Where would you like to go? (type a number that corresponds with box)')))
        while isEmpty(squareChosen) == False:
            print('Try another square')
            squareChosen=(int(input('Where would you like to go? (type a number that corresponds with box)')))
        if squareChosen == 1:
            square1 = 'X'
        elif squareChosen == 2:
            square2 = 'X'
        elif squareChosen == 3:
            square3 = 'X'
        elif squareChosen == 4:
            square4 = 'X'
        elif squareChosen == 5:
            square5 = 'X'
        elif squareChosen == 6:
            square6 = 'X'
        elif squareChosen == 7:
            square7 = 'X'
        elif squareChosen == 8:
            square8 = 'X'
        elif squareChosen == 9:
            square9 = 'X'
        if winner() is True:
            printBoard()
            break
        elif fullBoard(squareChosen) is True:
            printBoard()
            break
        computerTurn = randint(1,9)
        while isEmpty(computerTurn) == False:
            computerTurn = randint(1,9)
        if computerTurn == 1:
            square1 = 'O'
            print('The computer went', computerTurn)
        elif computerTurn == 2:
            square2 = 'O'
            print('The computer went', computerTurn)
        elif computerTurn == 3:
            square3 = 'O'
            print('The computer went', computerTurn)
        elif computerTurn == 4:
            square4 = 'O'
            print('The computer went', computerTurn)
        elif computerTurn == 5:
            square5 = 'O'
            print('The computer went', computerTurn)
        elif computerTurn == 6:
            square6 = 'O'
            print('The computer went', computerTurn)
        elif computerTurn == 7:
            square7 = 'O'
            print('The computer went', computerTurn)
        elif computerTurn == 8:
            square8 = 'O'
            print('The computer went', computerTurn)
        elif computerTurn == 9:
            square9 = 'O'
            print('The computer went', computerTurn)
        if winner() is True:
            printBoard()
            break
        elif fullBoard(squareChosen) is True:
            printBoard()
            break
    if winner() is True:
        print('We have a winner!')
    elif fullBoard(squareChosen) is True:
        print('No one wins :(')