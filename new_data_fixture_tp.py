# /usr/bin/python3

import mysql.connector
from faker import Faker

import random




TABLE_TRUNCATE=("utilisateur_groupe","utilisateur","groupe")

chaine_insert = ["INSERT INTO `utilisateur`(`nom`, `prenom`, `email`, `date_naissance`, `pays`, `ville`, `code_postal`,`telephoone`)VALUES (",")"]
CHAINE_INSERT_GROUPE=["INSERT INTO `groupe`(`nom`) VALUES (",")"]
CHAINE_INSERT_UTILISATEUR_GROUPE=["INSERT INTO `utilisateur_groupe`(`utilisateur_id`, `groupe_id`) VALUES (",")"]

conn = mysql.connector.connect(host="localhost", user="root", password="", database="test")
cursor = conn.cursor()
TAILLE_MAX_AL=int(input("entrer nombre de requete générée"))

def randomLength():
    rand = random.randint(0, 10)
    return (rand)


def generation(nb_generation, cpt):
    motif = "'"

    cpt += 1
    chaine_generated = ""

    generator = Faker()
    '''
    chaine_generated += motif
    chaine_generated+=str(cpt)
    chaine_generated += motif

    chaine_generated +=","+motif
    '''

    chaine_generated += "'"
    chaine_split = generator.name().split(" ")

    chaine_generated += chaine_split[0]
    chaine_generated += motif
    chaine_generated += "," + motif
    chaine_generated += chaine_split[1]
    chaine_generated += motif

    chaine_generated += "," + motif
    chaine_generated += generator.ascii_email()
    chaine_generated += motif
    chaine_generated += "," + motif
    chaine_generated += generator.date(pattern="%Y/%m/%d", end_datetime=None)
    chaine_generated += motif
    chaine_generated += "," + motif
    chaine_generated += generator.country()
    chaine_generated += motif
    chaine_generated += "," + motif
    chaine_generated += generator.city()
    chaine_generated += motif
    chaine_generated += "," + motif
    chaine_generated += generator.zipcode()
    chaine_generated += motif + ","
    chaine_generated += motif
    chaine_generated += generator.phone_number()
    chaine_generated += motif

    #debug
    #print(chaine_generated)

    return chaine_generated

def truncateTable():

    cursor.execute("SET FOREIGN_KEY_CHECKS=0")
    for i in range(len(TABLE_TRUNCATE)):
        cursor.execute("TRUNCATE TABLE "+TABLE_TRUNCATE[i])

    cursor.execute("SET FOREIGN_KEY_CHECKS=1")
    print("TABLE TRUNCATED "+str(TABLE_TRUNCATE))
    print("\n")

def genererGroupe(nb_groupe):

    groupe=[]
    data=""
    generator=Faker()
    for i in range(nb_groupe):
        data = generator.cryptocurrency_name()

        if data not in groupe:
             groupe.append(data)
        else:
            i-=1


    return groupe


def insertionGroupe(groupe):

    for i in range(len(groupe)):
        cursor.execute(CHAINE_INSERT_GROUPE[0] +"'"+ groupe[i] +"'"+ CHAINE_INSERT_GROUPE[1])
        print(CHAINE_INSERT_GROUPE[0] + groupe[i] + CHAINE_INSERT_GROUPE[1])

def insertionGroupeUtilisateur(utilisateur,groupe):

    aleatoire=0
    aleatoire2=0

    liste=[]
    print("insertion")
    for i in range(len(utilisateur)):

        aleatoire=random.randint(TAILLE_MAX_AL/2,TAILLE_MAX_AL*6)
        liste=[]
        print("insertion2")

        for e in range(aleatoire):

            print("insertion3")
            aleatoire2=random.randint(0,len(groupe))
            if aleatoire2 not in liste:
                print("insertion4")
                cursor.execute(CHAINE_INSERT_UTILISATEUR_GROUPE[0] +"'"+str(i)+"','"+ + CHAINE_INSERT_UTILISATEUR_GROUPE[1])
                liste.append(aleatoire2)
                print(CHAINE_INSERT_UTILISATEUR_GROUPE[0] +"'"+str(i)+"','"+ + CHAINE_INSERT_UTILISATEUR_GROUPE[1])
            else:
                print("insertion5")
                e-=1






def envoyer_requete(requete):

    for i in range(TAILLE_MAX_AL):
        chaine = generation(TAILLE_MAX_AL, i)
        cursor.execute(requete[0] + chaine + requete[1])
        print(i, "   ", chaine)

    return chaine


'''//////////////////////////////////////////////'''

utilisateur=[]
groupe_generated=[]

truncateTable()

groupe_generated=genererGroupe(random.randint(TAILLE_MAX_AL,TAILLE_MAX_AL*6))
print(groupe_generated)

insertionGroupe(groupe_generated)
chaine=envoyer_requete(chaine_insert)
insertionGroupeUtilisateur(utilisateur,groupe_generated)


conn.commit()
cursor.close()

conn.close()

'''
con=mysql

print("1")
#cursor=con.
print("2")
cursor.execute("INSERT INTO utilisateur(`id`, `nom`, `prenom`, `email`, `date_naissance`, `pays`, `ville`, `code_postal`) VALUES (1, 'Queen', 'Oliver', 'arrow@teamarrow.com', '1980/05/28', 'Na ilha', 'This City', '12345')")
print("3")

con.commit()
print("4")
cursor.close()
print("5")
con.close()
print("6")

for x in range(TAILLE_MAX_AL):
    print(randomLength())

'''

