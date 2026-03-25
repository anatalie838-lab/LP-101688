import os 
os.syste("cls")
#criando um vetor
vetor_nota = []
#adcionando 3 notas
for i in range(3):
    nota = float(input("digite sua nota: "))
    vetor_nota.append(nota)
#exibindo as notas informadas
    for i in range(3):
        print(f"nota: {vetor_nota[i]}")
