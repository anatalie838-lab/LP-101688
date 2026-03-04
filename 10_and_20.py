import os

os.system("cls")

verificação= int(input("Digite um numero de sua preferencia: "))

if verificação >= 10 and verificação <= 20:
    print("esta entre 10 e 20, passou! ")
else:
    print("nao esta entre os numeros solicitados")
