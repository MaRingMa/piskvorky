from supp import *
tahX = [None for x in range(50)]
tahY = [None for x in range(50)]
pt = -1

def main():
    while(input("Vložte 'y' pro hru, 'n' pro ukončení.") == "y"):
        d = deska()
        KK = True
        while True:
            if KK:
                znak = 1
            else:
                znak = 0
            print("hraje : {}".format(znak))
            KK = not(KK)
            d = Tah(d, znak)
            if (d == True):
                break
            vykresleni(d)
            a, msg = endOfGame(d)
            if a:
                print(msg)
                break
        print(tahX)
        print(tahY)
        print(pt)
    
    pass

def Tah(deska, znak):
    if (znak == 1):
        while True:
            x = int(input("x :"))
            if (x >= len(deska)):
                return True
            y = int(input("y: "))
            if (deska[x][y] is None):
                deska[x][y] = znak
                global pt
                global tahX
                global tahY
                pt = pt +1
                tahY[pt] = y
                tahX[pt] = x
                return deska
            print("Již obsazená pozice")
    else:
        minX, maxX, minY, maxY = minMax(deska)
        print("Min {}{}, Max {}{}".format(minX, minY, maxX, maxY))
        x,y, score = vyberStrat(deska, minX, minY, maxX, maxY)
        deska[x][y] = znak
        print("Vybrane X je {}\nVybrane Y je {}\nScore je {}".format(x,y, score))
        return deska

def vyberStrat(deska, minX, minY, maxX, maxY):
    xf = 0
    yf = 0
    score = 0
    for x in range(minX, maxX):
        for y in range(minY, maxY):
            if (deska[x][y] == None):
                sc = checkAround(deska, x, y, 1)
                sc = sc + (checkAround(deska, x, y, 0)/1.5)
                if (score < sc):
                    score = sc
                    xf = x
                    yf = y
    return xf, yf, score

def checkAround(deska, x, y, znak):
    score = 0
    xpom = x
    ypom = y
    multip = 1
    multipx = 2
    while (x >= 0 and deska[x-1][y] == znak): #vlevo
        score = 1*multip + score
        multip = multip * multipx
        x = x-1
    x = xpom
    multip = 1
    
    while (x <= len(deska)-1 and deska[x+1][y] == znak): # vpravo
        score = 1*multip + score
        multip = multip * multipx
        x = x +1
    x = xpom
    multip = 1

    while (y >= 0 and deska[x][y-1] == znak): #nahoru
        score = 1*multip + score
        multip = multip * multipx
        y = y -1
    y = ypom
    multip = 1

    while (y <= len(deska[0])-1 and deska[x][y+1] == znak): #dolu
        score = 1*multip + score
        multip = multip * multipx
        y = y +1
    y = ypom
    multip = 1

    while ((x <= len(deska)-1 and y >= 0) and deska[x+1][y-1] == znak):#vpravo nahoru
        score = 1*multip + score
        multip = multip * multipx
        x = x+1
        y = y-1
    x = xpom
    y = ypom
    multip = 1

    while ((x >= 0 and y >= 0) and deska[x-1][y-1] == znak):#vlevo nahoru
        score = 1*multip + score
        multip = multip * multipx
        x = x-1
        y = y-1
    x = xpom
    y = ypom
    multip = 1

    while ((x <= len(deska)-1 and y <= len(deska[0])-1) and deska[x+1][y+1] == znak):#vpravo dolu
        score = 1*multip + score
        multip = multip * multipx
        x = x+1
        y = y+1
    x = xpom
    y = ypom
    multip = 1
    
    while ((x >= 0 and y <= len(deska[0])-1) and deska[x-1][y+1] == znak):#vlevo dolu
        score = 1*multip + score
        multip = multip * multipx
        x = x-1
        y = y+1
    x = xpom
    y = ypom
    multip = 1

    
    return score

main()
