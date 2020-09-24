import random

def changeSpot(game,shape,x,y): ## fix this.
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
    return True

def computersTurn(): ## this will be a min/max algorithm - basically you will never win.
        ## min max. 
    print("min max")

def askPlayerWhere():
    x = input("select the x coordinate -")
    y = input("select the y coordinate -")
    x = int(x)
    y = int(y)

    if(x < 1 or x > 3 or y < 1 or y > 3):
        print ("invalid location.")
    else:
        print(x)
        print(y)
        changeSpot(x,y)


    
def playGame():
    ## set game variables
    game = [[0,0,0],
            [0,0,0],
            [0,0,0]]
    playerArray = ["na", "na"] ##first element is player one and 2 is player 2. 
    playerArray = selectWhoGoesFirst(playerArray)
    Player1 = playerArray[0]
    Player2 = playerArray[1]

    showBoard(game)
    while(True):## while the game is true - 
        ## who goes first? O goes first. 
        ## ask O to go first 
        ## change the spot on the board 
        ## check win 
        ## computers turn goes. 
        ## check win 
        ## ---- if there is a winner or no more spots - end game. 
        askPlayerWhere()

playGame()
