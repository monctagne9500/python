#!usr/bin/python3

import random
def exo1():
    for x in range(500):
        print("je dois faire des sauvegardes réguliéres de mas fichiers")

#exo1()

def exo2():
    cpt=0;
    for x in range(1000):
        if (x%2)!=0:
            print(x);


#exo1()
#exo2()

def exo3():

    for x in range(10):
        print(13*x)

#exo3()

def exo4():
    chaine=input("entrer un chaine e caractere")
    print(len(chaine))

#exo4()

#int() permet de caster une chaine en nombre
def exo5():
 nombre=input("entrer un nombre entier")
 if int(nombre)%2==0:
    print("ce nombre est pair")
 else:
    print("ce nombre est impair")

#exo5()

def exo6():

    flag=False
    while flag!=True:

        nombre = int(input("ecrire nombre entre 10 et 20"))
        if nombre>20:
            print("plus petit")

        if(nombre<10):
             print("plus grand")

        if(nombre<20 and nombre >10):
            flag=True

#exo6()

def exo8():
    valeur=int(input("entrer nombre depart"))
    for x in range(10):
        print(valeur*x)

#exo8()

def exo9():
    nombre=input("entrer valeur calcul factoriel")
    nombre=int(nombre)

    res=1

    for x in range(1,nombre+1):
        res*=x

    print(res)

#exo9()

def exo10():
    tab_asso={}
    tab_asso["poussin"]=6
    tab_asso["pupille"]=8
    tab_asso["minime"]=10
    tab_asso["cadet"]=12
    liste=[]

    nombre=int(input("entrer nombre entre 6 et 12"))



    for t in tab_asso.values():
        liste.append(t)

    for x in range(len(liste)):
        if x <len(liste):
            if nombre < liste[x] and nombre > liste[x + 1]:
                print(liste[x])
        else:
            print(liste(len(liste)))


#exo10()

def exo11():
    nb_art=int(input("entrer nombre article"))
    prix_art=int(input("entrer prix article"))
    TVA=0.2

    print("nombre d'articles= %i"%(nb_art))
    print("\n")
    print("prix HT : %f"%(prix_art))
    print("\n")
    prix_art=prix_art+prix_art*TVA
    print("prix TTC : %f"%(prix_art))


#exo11()

#exo12 voir exo9
''''
def exo13():
    res=""
    nombre=int(input("entrer nombre binaire"))

    while nombre!=0:
        if(nombre/2>0):
           nombre/=2
           res+="1"
        else:



    print(res)

#exo13()
'''
'''def exo14():
    for(i in range(1,1000):
        if i%3 ==0:
'''

'''def exo14():
    a=0
    b=1
    c=0
    nombre=int(input("enrer nombre "))

    for x in range(nombre):

'''

def exo16():

    val=0
    count=[]
    while True:
        val=val+1
        for i in range(1,19):
            if val%i == 0:
                count.append(1)
        if len(count) >= 19:
            print(val)
            break
    count=[]

#exo16()

def affichevie(nb):
    vie="*"
    res=""
    for x in range(nb):
        res+=vie

    return res

def tp2():

    tentative=9
    nombre_r=int(random.randint(1,100))


    while tentative!=0:
        print(affichevie(tentative))

        nombre=int(input("entrer nombre"))
        if nombre>nombre_r:
            print("trop grand\n")
            tentative-=1
        if(nombre<nombre_r):
            print("trop petit\n")
            tentative -= 1
        if nombre==nombre_r:
            print("bravo\n")
            break

#tp2()

def test():
    tuple=()
    tuple =("yolo","yit")
    
    print(tuple)

test()



