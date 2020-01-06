from array import array


def main():
    fichier = open("TP-DES\Messages\Clef_de_1.txt", "r")
    cleD = fichier.readline()
    fichier.close()
    cleF = ""
    print(len(cleD))
    print(cleD)
    i = 0
    dict = recupConstantesDES()
    for i in range(0, 63) :
        if i != 7 and i != 15 and i != 23 and i != 31 and i != 39 and i != 47 and i != 55:
            cleF = cleF + cleD[i]
    print(cleF)
main()