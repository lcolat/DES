from Extract_ConstantesDES import recupConstantesDES
from functions import *

def main():
    cleD = getCle()
    cleD = "0101111001011011010100100111111101010001000110101011110010010001"
    cleF = getFinalCle(cleD)
    dict = recupConstantesDES()
    arr = CLEF(cleD)
    arr2 = CP1(cleD, dict)
    g = getG(arr2)
    d = getD(arr2)
    arrk = []
    for i in range (0,16) :
        g = decallage(g)
        d = decallage(d)
        k = K1(g ,d, dict)
        arrk.append(k)
    m = "1101110010111011110001001101010111100110111101111100001000110010100111010010101101101011111000110011101011011111"
    m = mComplet(m)
    g = getGPaquetage(m)
    d = getDPaquetage(m)
    g = permutInit(g, dict)
    d = permutInit(d, dict)
    print(arrk)

main()