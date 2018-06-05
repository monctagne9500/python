#!/usr/bin/python3

text="je suis du texte"
print(text*3)

#Concatenation

text=text+" en plus"

print(text)

#////////////////////////////////////////

txt="hello world"

print(len(txt))

print(txt[1])

print(txt[0:5])

print("bonjour je m'appelle %s" %("Aurelien"))


print("bonjour je m'appelle %s" %(text))

#////////////////Echappement///////////////
print("////////////////Echappement///////////////")

text="je suis du \"texte\""
print(text)

# /////////////liste//////////////////
print(" /////////////liste//////////////////")

toto=1
maListe=[]
print(type(maListe))
maListe=[1,2,3]
print(maListe)

print("////////////////////////////////////////////")

maListe=[]
maListe.append(1)
print(maListe)
maListe.append("salut")
print(maListe)


print("///////////////////////////////////////")

maListe=["1 er", "deuxieme", "troisieme"]
print(maListe[1])
print(maListe[2])
maListe[1]="changement"
print(maListe)

print("supprimer element dans une liste")

maListe=["1 er","deuxieme","troisieme"]

#supprimé avec l'index

del maListe[1]

print(maListe)

#supprimer avec la valeur

maListe.remove("1 er")

print(maListe)