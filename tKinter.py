# /usr/bin/env python
#-*- coding: utf-8 -*-

'''from tkinter import *

fenetre = Tk()
label=Label(fenetre,text="Hello World")
label.pack()
fenetre.mainloop()'''

import os

liste_reseau=[]
subnet = "192.168.0."
for i in range(1, 255):
   hostname = subnet + str(i)
   response = os.system("ping -n 1 " + hostname)
   if response == 0:
      #print(hostname, 'is up!')
      liste_reseau.append(hostname)

print("RESULTAT\n")
print(liste_reseau)


