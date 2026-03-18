import os 

os.system ("cls")
#refaz
soma = 0  #
QUANTIDAADE_NOTAS: 2 #

for i in range(QUANTIDADE_NOTAS): #laço de repetição usado quando sabemos quantas vezes queremos repetir algo.

    while True: #
        nota = float(input("digite uma nota: ")) #

    if nota >= 0 and nota <= 10: #
        soma += nota #soma = soma + numero é a mesma coisa que soma += numero 
        break #
    else: #
     print("Nota invalida: ") #
     print("Tente novamente...") #

media = soma / QUANTIDADE_NOTAS #

print(f"media: {media}") #
