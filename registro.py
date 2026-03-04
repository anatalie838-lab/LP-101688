import os 
os.system("cls")

sexo = input ("Digite o gênero que você se identifica (M ou F): ")
ano = int(input("Digite o ano que você nasceu: "))

apto= 2026 - ano

sexo_apto = sexo == "M" or "m"

if sexo_apto and apto >= 18:
    print("Vai se apresentar para o serviço militar!")
else:
    print("você não está apto para servir ao serviço militar!")