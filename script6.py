#tri a bulle

liste=[1000,4,8,415,1,25,75,6]


print(liste)
print("\n")

for y in range(len(liste)):

 for x in range(len(liste)):

     if x<(len(liste)-1):


      if liste[x]>liste[x+1]:
         print("max= %i"%liste[x])
         m=liste[x+1]
         liste[x+1]=liste[x]
         liste[x]=m
         print(liste)
         print("\n")



print("fin"+"\n")
print(liste)

#tri par insertion
print("/////////////////tri par insertion////////////////\n")

chiffre=0
liste=[1000,4,8,415,1,25,75,6]
taille=len(liste)


def cherche_min(liste,nombre):
    print(liste[0:nombre])




