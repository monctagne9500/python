#/usr/bin/python3

import mysql.connector
from faker import Faker

import random







def randomLength():
    rand=random.randint(0,10)
    return (rand)










def generation(nb_generation,cpt):


    motif="'"



    cpt+= 1
    chaine_generated = ""

    generator = Faker()

    chaine_generated += motif
    chaine_generated+=str(cpt)
    chaine_generated += motif

    chaine_generated +=","+motif


    chaine_split=generator.name().split(" ")

    chaine_generated += chaine_split[0]
    chaine_generated += motif
    chaine_generated += "," + motif
    chaine_generated += chaine_split[1]
    chaine_generated += motif

    chaine_generated += "," + motif
    chaine_generated += generator.ascii_email()
    chaine_generated += motif
    chaine_generated += "," + motif
    chaine_generated+=generator.date(pattern="%Y/%m/%d", end_datetime=None)
    chaine_generated += motif
    chaine_generated += "," + motif
    chaine_generated+= generator.country()
    chaine_generated += motif
    chaine_generated += "," + motif
    chaine_generated+=generator.city()
    chaine_generated += motif
    chaine_generated += "," + motif
    chaine_generated+=generator.zipcode()
    chaine_generated += motif

     
 
    return chaine_generated









TAILLE_MAX_AL=50


chaine_insert=["INSERT INTO `utilisateur`(`id`, `nom`, `prenom`, `email`, `date_naissance`, `pays`, `ville`, `code_postal`) VALUES (",")"]






    #chaine=generation(TAILLE_MAX_AL,i)

   # print("\n"+chaine)

conn = mysql.connector.connect(host="localhost",user="root",password="", database="test")


cursor = conn.cursor()




for i in range(TAILLE_MAX_AL):

    chaine = generation(TAILLE_MAX_AL,i)
    cursor.execute(chaine_insert[0] + chaine +chaine_insert[1])
    print(i,"   ", chaine )

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