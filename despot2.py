import random
import sys
n= random.randint(0,9)
b= int(input("donner un nombre comprise entren 0 et 9"))
for b in range(3):
  if b == n:
   print("felicitation")
else:
    print("veillez saisir un nombre svp")
    sys.exit()


