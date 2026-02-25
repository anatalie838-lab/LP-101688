import os 
os.system ("cls")

numero_primeiro = int(input("digite um numero: "))
numero_segundo = int(input("digite o segundo numero: "))


soma = numero_primeiro + numero_segundo 

media = soma / 2 

produto = numero_primeiro * numero_segundo 

if numero_primeiro > numero_segundo:
    menor = numero_segundo 
    maior = numero_primeiro 

else: 
    menor = numero_primeiro 
    maior = numero_segundo 

print(media)
print(soma)
print(produto)
print(maior)
print(menor)

if numero_primeiro == numero_segundo:
       valor_igual = print("os valores informados sao iguais")
else:
        valor_diferente = print("os valores informados  sao diferentes")
