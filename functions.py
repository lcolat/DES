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

def decallage(d) :
    t = d[0]
    d = d.replace(t, '', 1) + t
    return d

def K1(g, d, dict) :
    k = g + d
    arr =[]
    for i in range(0, 48) :
        arr.append(k[dict['CP_2'][0][i]])
    k = ""
    for i in range(0, 48):
        k = k + arr[int(i)]
    return k

def mComplet(m):
    while len(m) < 128 :
        m = m +"0"
    return m

def getGPaquetage(m) :
    d = ""
    for i in range (0,64) :
        d = d + m[i]
    return d

def getDPaquetage(m) :
    d = ""
    for i in range (64,128) :
        d = d + m[i]
    return d

def permutInit(g, dict) :
    k = ""
    for i in range(0, 64):
        k = k + g[dict['PI'][0][i]]
    return k
