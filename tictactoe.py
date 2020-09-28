import random

def changeSpot(game,shape,spot): ## fix this.
    x = spot[0]
    y = spot[1]
    print("change spot - " + shape)
    game[y-1][x-1] = shape 
    showBoard(game)

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

def checkWin():
    print("hello")
    return True

def checkTie():
    return True

def checkIfGameisOver():
    checkWin()
    checkTie()

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
    game = [["-","-","-"],
            ["-","-","-"],
            ["-","-","-"]]
    
    player = "X"
    player2 = "O"

    showBoard(game)


    while(True):## while the game is true - 
        ## who goes first? O goes first. 
        ## ask O to go first 
        ## change the spot on the board 
        ## check win 
        ## computers turn goes. 
        ## check win 
        ## ---- if there is a winner or no more spots - end game. 
        return

playGame()
