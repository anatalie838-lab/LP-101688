import os 
os.system("cls")

# media=float(input("Digite a sua nota: "))

# if media >= 7 and media <= 4:
#     print ("Aprovado. Você passou!")
# else:
#     print ("Você foi reprovado!")
# elif 
#     print ("Você esta em recuperação!")    
soma = 0 
QUANTIDADE_NOTAS = 3

for i in range (QUANTIDADE_NOTAS ):
    nota= int(input("digite uma nota: "))
    soma += nota 
media = soma / QUANTIDADE_NOTAS 
print(f"media: {media}")

if media >= 7:
    resultado="aprovado"
elif media <= 4:
    resultado="reprovado"
else:
    resultado="recuperação"
