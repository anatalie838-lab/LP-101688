import os 
import time 

os.system("cls")

# #de 1 ate 10 
# for i in range(1, 11, 1):
#     print(i)

#     time.sleep(2) #espera ate 2 

#de 10 ate 1 
# for i in range(100, 121, 2): 
#     print(i)

#     time.sleep(2) #espera ate 2 

# for i in range(1, 21, 2): 
#     print(i)

#     time.sleep(2) #espera ate 2 

n = int(input("digite um numero: "))

for n in range(n, 0, -1):  #esse "n" ai é da varivel, se for com "i" vai ser aq e no print tb. e o nome da variavel que vem depois do for rtem que ser o mesmo que vai no print  
    print(n)
    time.sleep(1)
