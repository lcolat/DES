def getCle():
    fichier = open("TP-DES\Messages\Clef_de_1.txt", "r")
    cleD = fichier.readline()
    fichier.close()
    return cleD

def getFinalCle(cleD):
    cleF =""
    for i in range(0, 63) :
        if i != 7 and i != 15 and i != 23 and i != 31 and i != 39 and i != 47 and i != 55:
            cleF = cleF + cleD[i]
    return cleF

def CLEF(cleD):
    arr = []
    for i in range (0,63) :
        arr.append(cleD[i])
    return arr

def CP1(cleD, dict) :
    arr = []
    for i in range(0, 56) :
        arr.append(cleD[dict['CP_1'][0][i]])
    return arr

def getD(arr) :
    d = ""
    for i in range (28,56) :
        d = d + arr[i]
    return d

def getG(arr) :
    g = ""
    for i in range(0, 28) :
        g = g + arr[i]
    return g
