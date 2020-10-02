import random

def changeSpot(spot, board, player):
    spot = int(spot)
    if spot < 1 or spot > 9:
        print("invalid")
    else:
        if(spot == 1):
            board[0][0] = player
        elif(spot == 2):
            board[0][1] = player
        elif(spot == 3):
            board[0][2] = player
        elif(spot == 4):
            board[1][0] = player
        elif(spot == 5):
            board[1][1] = player
        elif(spot == 6):
            board[1][2] = player
        elif(spot == 7):
            board[2][0] = player
        elif(spot == 8):
            board[2][1] = player
        elif(spot == 9):
            board[2][2] = player
        showBoard(board)
        

def selectWhoGoesFirst(player):
    n = random.randint(1,2)
    if n == 1:
        player  = "X"
    else:
        player  = "O"
    return player

def showBoard(game):
    for row in game:
        print(row)

def checkWin(board, winner):
    ## check horzontals 
    if(board[0][0] == board[0][1] == board[0][2]):
        print(winner + " wins")
        return True
    elif(board[1][0] == board[1][1] == board[1][2]):
        print(winner + " wins")
        return True
    elif(board[2][0] == board[2][1] == board[2][2]):
        print(winner + " wins")
        return True

    ## check verticals 
    elif(board[0][0] == board[1][0] == board[2][0]):
        print(winner + " wins")
        return True
    elif(board[0][1] == board[1][1] == board[2][1]):
        print(winner + " wins")
        return True
    elif(board[0][2] == board[1][2] == board[2][2]):
        print(winner + " wins")
        return True

    ## check diagnols 
    elif(board[0][0] == board[1][1] == board[2][2]):
        print(winner + " wins")
        return True
    elif(board[0][2] == board[1][1] == board[2][0]):
        print(winner + " wins")
        return True
    else:
        return False

def checkTie(board):
    for row in board:
        for value in row:
            if(value != "X" and value != "O"):
                return False
    print(" its a tie ")
    return True
            

def checkIfGameisOver(board, XorO):
    if(checkWin(board, XorO)):
        return True
    elif (checkTie(board)):
        return True
    else:
        return False

def computersTurn(): ## this will be a min/max algorithm - basically you will never win.
        ## min max. 
    print("min max")

def askPlayerWhere():
    x = input("select the x coordinate -")
    y = input("select the y coordinate -")
    x = int(x)
    y = int(y)
    spot = [x,y]

    if(x < 1 or x > 3 or y < 1 or y > 3):
        print ("invalid location.")
        askPlayerWhere()
    else:
        print(x)
        print(y)
        return spot


    
def playGame():
    ## set game variables
    game = [
            ["1","2","3"],
            ["4","5","6"],
            ["7","8","9"]
           ]
    turn = 1
    showBoard(game)
    isGameOver = False

    while(not isGameOver):## while the game is true - 
        XorO = "X"
        if(turn%2 != 0):
            XorO = "X"
        else:
            XorO = "O"
        spot = input("select where to go 1-9 - ")

        changeSpot(spot, game, XorO)
        isGameOver = checkIfGameisOver(game, XorO)
        turn = turn + 1
    print(" - game over - ")

playGame()
