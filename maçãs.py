import os
os.system ("cls")

print("entre na minha loja de maçãs e veja as grandes novidades")
print("caso desejar menos de 12 maçãs o preço por unidade sera de 1,30")
print("caso desejar mais de 12 maçãs o preço sera de 1,00")

quantidade = int(input("/nInsira a quantidade que deseja comprar de maçãs:"))

if quantidade >= 12:
    valor_maca = quantidade * 1.00
    print("\no valor por maçã sai por R$1,00")
    print("\nO total é: {valor_maca}") 
else:
     valor_maca = quantidade * 1,30
     print("\n*O valor por maçã é R$ 1,30*")
     print(f"\n--O total é: R$ {valor_maca:.2f}--")

