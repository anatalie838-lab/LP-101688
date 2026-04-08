import os 


#função sem parametro e sem retorno 
def logo(): 
    os.system ("cls")
    print("======")
    print("  SENAI  ")
    print("======")

#função com paramentros e com retorno

def somar(a, b):
    return a + b
logo()
print("Solicitando dados")
n1 = int(input("digite o primeiro numero: "))
n2 = int(input("Digite o segundo numero: "))

soma = somar(n1, n2)

logo()
print("Exibindo dados")
print(f"soma: {soma}")

#função ainda com paramentros e retorno so que subtração

def subtrair(a, b):
    return a - b
logo()
print("solicitando os dados: ")
n1 = int(input("Digite o primeiro numero: "))
n2 = int(input("Digite o segundo numero: "))

subtrair = subtrair(n1, n2)

logo()
print("exibindo dados")
print(f"subtrair: {subtrair}")


#função com paramentro e sem retorno

def multiplicar(a, b):
    multiplicacao = a * b
print(f"multiplicacao: {multiplicacao}")






