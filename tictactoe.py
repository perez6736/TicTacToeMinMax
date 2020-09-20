import random

x = 0
y = 0
gameStatus = False
player1Turn = False
player2Turn = False
ComputersTurn = False

def changeSpot(game,shape,x,y):
    print("change spot - " + shape)
    game[y-1][x-1] = shape 
    showBoard(game)

def selectWhoGoesFirst(playerArray):
    n = random.randint(1,2)
    if n == 1:
        playerArray[0]  = "X"
        playerArray[1]  = "O"
    else:
        playerArray[0]  = "O"
        playerArray[1]  = "X"
    return playerArray

def showBoard(game):
    for row in game:
        print(row)

def checkWin(game):
    print("hello")

def computersTurn(): ## this will be a min/max algorithm - basically you will never win.
        ## min max. 
    print("min max")

def askPlayerWhere(game, playerArray, turn): ## used recursion casue why not? 
    ## check who goes first 
    if(playerArray[0] == "X"): ## if player is X then computer is O and he goes 
        ##do computers turn 
        print("do computer stuff")
        turn = turn + 1
        askPlayerWhere(game, playerArray,turn)
    else:
        x = input("select a x spot on board.")
        x = int(x)
        if(x>0 and x<4): ## check range 
            y = input("select a y spot on board.")
            y = int(y)
            if(y>0 and y<4):
                changeSpot(game,playerArray[turn],x,y)
                turn = turn + 1
                if(!checkWin(game)):
                    ## computersTurn -  need to wirte this 
            else:
                print("invalid value")
                askPlayerWhere(game, playerArray,turn)
        else:
            print("invalid value")
            askPlayerWhere(game, playerArray,turn)
    
def playGame():
    game = [[0,0,0],
        [0,0,0],
        [0,0,0]]
    playerArray = ["na", "na"] ##first element is player one and 2 is player 2. 
    gameStatus = True
    showBoard(game)
    selectWhoGoesFirst(playerArray)
    while(gameStatus):
        askPlayerWhere(game,playerArray,1)

playGame()
