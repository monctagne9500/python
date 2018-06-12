#/usr/bin/python3
#crypto_ascii




def getAsciiConversion(chaine):

    cpt=1
    print(chaine)
    taille_lim=len(chaine)
    chaine_convertie=""

    for i in range(taille_lim):


     if cpt==1:

            if i<(taille_lim-2):


             data = chaine[i:i+2]
             print(data)


             #chaine = chr(int(data, 16))

             character=str(data)
             print(character)
             chaine_convertie += character
             cpt+=1
     cpt += 1
    return chaine_convertie







CHAINE_DECO="4C6520666C6167206465206365206368616C6C656E6765206573743A203261633337363438316165353436636436383964356239313237356433323465"

print(getAsciiConversion(CHAINE_DECO))









