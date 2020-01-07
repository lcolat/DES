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
main()