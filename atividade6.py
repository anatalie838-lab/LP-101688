import os 

os.system("cls")

soma = 0 

# for i in range (5):
#     nota= int(input("digite uma nota: "))
#     soma += nota 
# media = soma / 5
# print(f"media: {media}")

# pode tambem ser desse jeito usando constantes, que são escritas em capslock. isso simplifica o código em caso de necessidade de mudanças futuras. 
soma = 0 
QUANTIDADE_NOTAS = 5 

for i in range (QUANTIDADE_NOTAS ):
    nota= int(input("digite uma nota: "))
    soma += nota 
media = soma / QUANTIDADE_NOTAS 
print(f"media: {media}")
