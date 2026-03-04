import os 

os.system("cls")

media=float(input("Digite a sua nota: "))
faltas=int(input("Qual seu numero de faltas? "))

if media >= 7 and faltas <= 40:
    print ("Aprovado.Você passou!")
else:
    print ("Você foi reprovado! Se saia logo vá")