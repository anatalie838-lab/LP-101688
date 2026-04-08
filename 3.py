import os
os.system("cls")

def reajustar_preco(preco):
    if preco < 100:
        return preco * 1.10
    else:
        return preco * 1.20
valor = float(input("Digite o preço: "))
novo_preco = reajustar_preco (valor)
print(f"o novo preço é: R$ {novo_preco}: 2f")