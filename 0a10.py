import os

os.system("cls")

nota=float(input("Digite a sua nota: "))
if nota >= 0 and nota <= 10:
    print(f"a sua nota é: {nota}")
else:
    print("a nota informada deve ser entre 0 a 10") 
