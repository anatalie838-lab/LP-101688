import os
import time 
os.system ("cls")

soma = 0 

for i in range (5):
    numero = int(input("digite um número: "))
    #soma = soma + numero é a mesma coisa que soma += numero 
    soma = soma + numero
    print(f"soma: {soma}")

