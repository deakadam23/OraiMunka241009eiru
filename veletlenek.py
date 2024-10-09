import random

from beolvas import *
from random import *
def egyAlapA():
 szam1 = beolvasEgesz()
 if szam1%2 == 1:
     print("Páratlan")
 else:
       print("Páros")

def egyAlapB():

 szam1 = randint(-10,10)
 #print("szam:"+str(szam1))
 while not (szam1%2==0):
  szam1 = randint(-10,10)
 #print(szam1)
 print(szam1**2)

def EgyAlapC():
    szam1 = generalParatlanEgesz()
    print(szam1 ** 2)

def kettoAlapA():
szam1 = beolvasEgesz()
if szam1 >=1 and szam1<=12:
 if szam1 == 1:
   print("Január")
 elif szam1 == 2:
  print("Február")
 elif szam1 == 3:
  print("Március")
 elif szam1 == 4:
     print("Április")
 elif szam1 == 5:
    print("Május")
 elif szam1 == 6:
  print("Június")
 elif szam1 == 7:
  print("Július")
elif szam1 == 8:
 print("Augusztus")
elif szam1 == 9:
 print("Szeptember")
elif szam1 == 10:
 print("Október")
elif szam1 == 11:
 print("November")
elif szam1 == 12:
 print("December")

else:
    print("Hiba!: Nem megfelelo szam")