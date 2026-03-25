import os 
import os 
os.syste("cls")
#criando um vetor
vetor_nota = []
QUANTIDADE_DE_NOTAS = 3
#adcionando 3 notas
print(f"adcionando{QUANTIDADE_DE_NOTAS}notas")
for i in range(3):
    nota = float(input("digite sua nota: "))
    #adcionando nota no vetor 
    vetor_nota.append(nota)
#sum(vetor)= soma todos os valores no vetor
    media = sum (vetor_nota)/QUANTIDADE_DE_NOTAS

    print(\nExibindo as notas informadas)
#ForEach percorre o vetor sem informar a quanidade 
# enumerate = atraves da variavel i numera a quantidade de repetição
for i, uma_nota enumerate(vetor_nota, start=1):
    print(f"{i}ª nota: {uma_nota} ")

    print(media: {media})
