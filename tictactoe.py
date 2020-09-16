import random

game = [[0,0,0],
        [0,0,0],
        [0,0,0]]
playerShape = "na"
computerShape = "na"
x = 0
y = 0
gameStatus = False
player1Turn = False
player2Turn = False
ComputersTurn = False

def changeSpot(x,y):
    game[y-1][x-1] = playerShape 
    showBoard()

def selectWhoGoesFirst():
    n = random.randint(1,2)
    if n == 1:
        playerShape = "X"
        computerShape = "O"
    else:
        playerShape = "O"
        computerShape = "X"
    print("you are " + playerShape)

def showBoard():
    for row in game:
        print(row)

def checkWin():
    print("hello")

def computersTurn(): ## this will be a min/max algorithm - basically you will never win.
        ## min max. 
    print("min max")

def askPlayerWhere(): ## used recursion casue why not? 
    x = input("select a x spot on board.")
    x = int(x)
    if(x>0 and x<4): ## check range 
        y = input("select a y spot on board.")
        y = int(y)
        if(y>0 and y<4):
            changeSpot(x,y)
            ## checkwin() - need to wirte this
            ## computersTurn -  need to wirte this 
            return
        else:
            print("invalid value")
            askPlayerWhere()
    else:
        print("invalid value")
        askPlayerWhere()
    

def playGame():
    gameStatus = True
    showBoard()
    selectWhoGoesFirst()
    while(gameStatus):
        askPlayerWhere()

playGame()
