import os 
os.system("cls")

#funções sem retorno 

def somar(n1, n2):
    soma = n1 + n2 
    print(f"soma: {soma}")

#exemplo de uso da função 
n1 = int(input("digite o primeiro numero: "))
n2 = int(input("digite o segundo numero: "))

#chamando a função
#enviando parametros 
somar(n1, n2)
