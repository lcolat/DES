from Extract_ConstantesDES import recupConstantesDES
from functions import *
from ConvAlphaBin import *

def main():
    """arr = cryptage()"""
    arr = ['','']
    arr[0] = ''
    for i in txt0 :
        arr[0] = arr[0] + conv_bin(i)
    arr[1] = getCle()
    decryptage(arr[0], arr[1])
main()