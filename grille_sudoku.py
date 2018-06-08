#! /usr/bin/python3
#hola

import random

case_init=list(range(9))
grille=[]
liste_aleatoire=[]

#
def init_case():
 ''' for x in range(len(case)):
     case[x]=case_init
'''
 for x in range(len(case_init)):
     case_init[x]=0

 for x in range(len(case_init)):
     grille.append(case_init[:])

#
def affiche(grille):
    for case in grille:
       print(case)

#
def init_aleatoire():

    choix=[]

    nombre_aleatoire=random.randint(10,20)

    print("\n")
    print(nombre_aleatoire)


    for x in range(nombre_aleatoire):
         liste_aleatoire.append(random.randint(1,9))

    print(liste_aleatoire)

    for x in range(nombre_aleatoire):

        if x < nombre_aleatoire-1:
            if liste_aleatoire[x] == liste_aleatoire[x+1]:
                if liste_aleatoire[x+1]!=9:
                    liste_aleatoire[x+1]+=1
    print("\n")
    print("liste_aleatoire modifié\n")
    print(liste_aleatoire)
#
def coordonnees_aleatoire():

    coord=[]




    for i in range(2):

        coord.append(random.randint(0,8))

    return coord

#
def remplissage_grille(grille):

    flag=True
    cpt=0
    chiffre=0



    '''tant que flag == True'''

    while flag:


        coord_aleatoire=coordonnees_aleatoire()
        chiffre=liste_aleatoire[0]

        #print(grille[coord_aleatoire[0]][coord_aleatoire[1]])

        flag_ok=True

        if grille[coord_aleatoire[0]][coord_aleatoire[1]]==0:


            for y in range(len(grille)):

               # print(y, coord_aleatoire[1], "    ", coord_aleatoire[0], y)

                if (grille[y][coord_aleatoire[1]] == chiffre) and grille[coord_aleatoire[0]][y] == chiffre:
                    #if (grille[y][coord_aleatoire[1]] == chiffre) and grille[coord_aleatoire[0]][y] == chiffre:
                    flag_ok=False
                    print("/")


            print("\n")








        #if flag_ok==True
        if flag_ok:

            grille[coord_aleatoire[0]][coord_aleatoire[1]]=liste_aleatoire[0]
            del liste_aleatoire[0]
            print(liste_aleatoire,"\n")
            cpt+=1

        if len(liste_aleatoire)==0:
            flag=False

















init_case()

affiche(grille)

init_aleatoire()

remplissage_grille(grille)

print("\nRESULTAT\n")

affiche(grille)











