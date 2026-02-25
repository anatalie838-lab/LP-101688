import os 
os.system("cls")

idade = int(input("digite sua idade"))

if idade < 16:
    print("voce ainda noa pode votar!")
elif idade == 16 or 17:
    print("voto opcional!")     
if idade > 18: 
    print("voce é obrigado a votar!")
if idade > 65:
    print("voce não precisa mais votar!")        