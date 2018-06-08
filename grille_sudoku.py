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
    chiffre = 0
    coord = []

    '''tant que flag == True'''

    while flag:
        

        coord_aleatoire=coordonnees_aleatoire()
        #print(coord_aleatoire)
        #print(grille[coord_aleatoire[0]][coord_aleatoire[1]])

        for x in range(len(grille)):

            for y in range(len(grille)):



                if grille[coord_aleatoire[0]][coord_aleatoire[1]]==0:
                    if grille[coord_aleatoire[0]][y]!= chiffre:




                           # print(coord_aleatoire[0],cpt)



                            # print(liste_aleatoire)
                            grille[coord_aleatoire[0]][coord_aleatoire[1]]=liste_aleatoire[0]
                            grille[coord[0]][coord[1]] = chiffre
                            del liste_aleatoire[0]
                            cpt+=1

                if len(liste_aleatoire)==0:
                    flag=False

















'''def remplissage_grille(grille,liste_aleatoire):

    coord=[]
    chiffre=0
    cpt=0

    for i in range(len(liste_aleatoire)):

     chiffre=liste_aleatoire[i]
     coord=coordonnees_aleatoire()
     for x in range(len(grille)):

       #for y in range(len(grille)):

      if grille[coord[0]][coord[1]]== 0:
                grille[coord[0]][coord[1]]=chiffre
                #del liste_aleatoire[i]



'''






#
init_case()

affiche(grille)

init_aleatoire()

remplissage_grille(grille)

affiche(grille)







remplissage_grille(grille,liste_aleatoire)

print("/////////////////////\n")

affiche(grille)









