import os 

os.system("cls")

import time 

numero = int(input("informe o numero que deseja: "))

for i in range (numero, -1, -1):
    print(i)
    time.sleep(2)