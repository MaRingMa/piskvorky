def deska(): #49/49
    desk = [[None for x in range(49)] for y in range(49)]
    return desk

def omezeniVykresleni(Min, Max, deska):
    if(Min -2 >= 0):
        Min = Min -2
    elif(Min -1 >= 0):
        Min = Min -1
    if(Max +2 < len(deska)):
        Max = Max +2
    elif(Max +1 < len(deska)):
        Max = Max +1
    return Min, Max

def minMax(ActualStatus):
    xMin = len(ActualStatus) -1
    xMax = 0
    yMin = len(ActualStatus[0]) -1
    yMax = 0
    for y in range(len(ActualStatus[0])):
        for x in range(len(ActualStatus)):
            if (ActualStatus[x][y] != None):
                if(x > xMax):
                    xMax = x
                if(x < xMin):
                    xMin = x
                if(y > yMax):
                    yMax = y
                if(y < yMin):
                    yMin = y
    for i in range(3):
        if(xMin-i >=0):
            xMin = xMin-i
        if(yMin-i >=0):
            yMin = yMin-i
        if(xMax+i <len(ActualStatus)):
            xMax = xMax+i
        if(yMax+i <len(ActualStatus[0])):
            yMax = yMax+i
    return xMin, xMax, yMin, yMax

def vykresleni(ActualStatus):
    xMin, xMax, yMin, yMax = minMax(ActualStatus)    
    xMin, xMax = omezeniVykresleni(xMin, xMax, ActualStatus)
    yMin, yMax = omezeniVykresleni(yMin, yMax, ActualStatus[0])
    print(" \t", end = "|")
    for x in range(xMin, xMax+1):
        print( x, end = "|")
    print("\n\t---", end = "")
    for x in range(xMin, xMax+1):
        print("--", end = "")
    print()
    for y in range(yMin, yMax+1):
        print(y, end= "\t|")
        for x in range(xMin, xMax+1):
            if (ActualStatus[x][y] == None):
                print(" ", end = "|")
            else:
                print(ActualStatus[x][y], end = "|")
        print()

def checkX(deska, x, y): # pouze do len-5
    for i in range(5):
        if (deska[x+i][y] != deska[x][y]):
            return False
    return True

def checkY(deska, x, y):
    for i in range(5):
        if (deska[x][y+i] != deska[x][y]):
            return False
    return True

def checkXY(deska, x, y):
    for i in range(5):
        if(deska[x+i][y+i] != deska[x][y]):
            return False
    return True

def checkYX(deska, x, y):
    for i in range(5):
        if (deska[x+i][y-i] != deska[x][y]):
            return False
    return True

def check(deska, x, y):
    if (checkX(deska, x, y) or checkY(deska, x, y) or checkXY(deska, x, y) or checkYX(deska, x, y)):
        return True
    return False

def endOfGame(deska):
    for x in range(len(deska)):
        for y in range(len(deska[0])):
            if (deska[x][y] is not None):
                if (check(deska,x,y) == True):
                    return True, "Vítězí : {}".format(deska[x][y]) 
    return False, ""
