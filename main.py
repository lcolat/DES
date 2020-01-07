from Extract_ConstantesDES import recupConstantesDES

def main():
    fichier = open("TP-DES\Messages\Clef_de_1.txt", "r")
    cleD = fichier.readline()
    fichier.close()
    cleD = "0101111001011011010100100111111101010001000110101011110010010001"
    cleF = ""
    print(len(cleD))
    print(cleD)
    i = 0
    dict = recupConstantesDES()
    arr = []
    arr2 = []
    for i in range(0, 63) :
        if i != 7 and i != 15 and i != 23 and i != 31 and i != 39 and i != 47 and i != 55:
            cleF = cleF + cleD[i]
    for i in range (0,63) :
        arr.append(cleD[i])
    for i in dict['PI'][0] :
        arr2.append(cleD[dict['PI'][0][i]])
    print(cleF)
    print(arr)
    print (arr2)
    print(dict['PI'])
    print(cleD[dict['PI'][0][0]])
    print(cleD[57])
main()