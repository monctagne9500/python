#! /usr/bin/python3
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
     grille.append(case_init)

#
def affiche(grille):
    for case in grille:
       print(case)

#
def init_aleatoire():

    nombre_aleatoire=random.randint(1,20)

    for x in range(nombre_aleatoire):
        liste_aleatoire.append(random.randint(1,9))

print(liste_aleatoire)
#

init_case()
affiche(grille)
init_aleatoire()