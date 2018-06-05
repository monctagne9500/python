#!/usr/bin/python3

import random

maListe=["1 er","deuxieme","troisieme"]
secondeList=maListe
maListe[0]="toto"
print(secondeList)

print("///////////////copie liste//////////////")

maListe=["1 er","deuxieme","troisieme"]
secondeList=maListe[:]
maListe[0]="toto"
print(secondeList)

print("////////////////tuple/////")

monTuple=()
print(type(monTuple))
monTuple=("toto",)
print(type(monTuple))

""" affiche une erreur
monTuple[0]="error
"""

print("//////////monDico/////////////")

monDico={}
monDico["name"]="jfhh"
monDico["heigth"]="gjghg"

#fonction
print("//////////////fonction///////////")

def mafonction():
    print("salut les gens")

mafonction()

def mafonction2(param):
    print(param)


mafonction2("ghyugh")

#fonction splat

def splat(*lot):
    for t in lot:
        print(t)

        splat(1,2,"hugug")





#fonction


#fonction input

valeur=input("enter your value")

#fonction random()

random.choice([1,2,3,4,5])





