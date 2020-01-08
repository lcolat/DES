from ConvAlphaBin import *
from Extract_ConstantesDES import recupConstantesDES

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
    arr = []
    t = ""
    j = 0
    for i in range (0,len(m)):
        t = t + m[i]
        if len(t) == 128:
            arr.append(t)
            t = ""
            j = j + 1
    while len(arr[j-1]) < 128:
        arr[j-1] = arr[j-1] + "0"
    return arr

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

def getGRonde(s) :
    k = ""
    for i in range(0, 32):
        k = k + s[i]
    return k

def getDRonde(s) :
    k = ""
    for i in range(32, 64):
        k = k + s[i]
    return k

def expantion(g, dict) :
    k = ""
    for i in range(0, 48):
        k = k + g[dict['E'][0][i]]
    return k

def ouAvecCle(g, arr):
    k = ""
    for i in range(0, 48):
        if (g[i] == "0" and arr[i] == "0") or (g[i] == "1" and arr[i] == "1"):
            k = k + "0"
        else :
            k = k + "1"
    return k

def decoupe(g, dict) :
    k = ""
    t = ""
    a = ""
    b = ""
    c = ""
    j = 0
    for i in range(0,48) :
        k = k + g[i]
        if len(k) == 6 :
            a = int(k[0] + k[5],2)
            b = int(k[1] +k[2] +k[3] + k[4],2)
            c = str(bin(dict['S'][j][a][b]))
            c = c.replace("0b", "")
            while len(c) < 4:
                c = "0" + c
            t = t + c
            j = j + 1
            k = ""
    return t

def permutRonde(g, dict) :
    k = ""
    for i in range(0, 32):
        k = k + g[dict['PERM'][0][i]]
    return k

def dernierOu(g, d) :
    k = ""
    for i in range(0, 32):
        if (g[i] == "0" and d[i] == "0") or (g[i] == "1" and d[i] == "1"):
            k = k + "0"
        else :
            k = k + "1"
    return k

def permutInitI(g, dict) :
    k = ""
    for i in range(0, 64):
        k = k + g[dict['PI_I'][0][i]]
    return k

def cryptage():
    cleD = getCle()
    cleD = "0101111001011011010100100111111101010001000110101011110010010001"
    cleF = getFinalCle(cleD)
    dict = recupConstantesDES()
    arr = CLEF(cleD)
    arr2 = CP1(cleD, dict)
    transg = ""
    transd = ""
    t=""
    g = getG(arr2)
    d = getD(arr2)
    arrk = []
    for i in range(0, 16):
        g = decallage(g)
        d = decallage(d)
        k = K1(g ,d, dict)
        arrk.append(k)
    m = conv_bin(txt0)
    arrm = []
    arrm = mComplet(m)
    for n in arrm:
        g = getGPaquetage(n)
        d = getDPaquetage(n)
        g = permutInit(g, dict)
        d = permutInit(d, dict)


        for i in range(0, 16):
            gg = getGRonde(g)
            gd = getDRonde(g)
            dg = getGRonde(d)
            dd = getDRonde(d)

            transg = gd
            transd = dd

            gd = expantion(gd, dict)
            dd = expantion(dd, dict)

            gd = ouAvecCle(gd, arrk[i])
            dd = ouAvecCle(dd, arrk[i])

            gd = decoupe(gd, dict)
            dd = decoupe(dd, dict)

            gd = permutRonde(gd, dict)
            dd = permutRonde(dd, dict)


            gd = dernierOu(gg, gd)
            gg = transg
            dd = dernierOu(dg, dd)
            dg = transd


            g = gg + gd
            d = gd + dd
        g = permutInitI(g, dict)
        d = permutInitI(d, dict)
        t = t + g + d
    print("texte crypté : " + t)
    print("clef de décryptage : " + cleF)