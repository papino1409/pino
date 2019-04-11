mport random
import sys
n= random.randint(0,9)
b= int(input("donner un nombre comprise entren 0 et 9"))
while True:
 if b == n:
  print("felicitation")
 else:
  print("veillez saisir un nombre svp")
  sys.exit()



