#!/usr/bin/python3

class Toto:
   def __init__(self):
          self.nom="ferrari"
   def chnageNomVoiture(self,nom):
      self.nom=nom

maVoiture=Toto()
print(maVoiture.nom)
maVoiture.chnageNomVoiture("totyota")
print(maVoiture.nom)
