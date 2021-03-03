#Calcula indice de masa corporal
import math 
libreria=math
Peso=0
Altura=0
Peso=int(input("cual es su peso"))
Altura=float(input("cual es su altura"))
IMC= Peso / libreria.pow(Altura,2)
#IMC= Peso / (Altura**2) 
print (IMC)