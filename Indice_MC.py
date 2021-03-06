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
if IMC <18.5 :
    print("Bajo Peso")
elif IMC >=18.5 or IMC <= 24.9:
    print("Normal")
elif IMC >=25.0 or IMC <= 29.9:
    print("Sobrepeso")
elif IMC >= 30.0:    
    print("Obeso")      
else : 
    print("fuera de rango")
