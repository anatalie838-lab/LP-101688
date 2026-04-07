import os 

os.system("cls")

#funções sem retorno 

def tabuada(numero):
    for i in range(1,11):
     print(f"{numero} x {i} = {numero * i}")

#exemplo de uso da função 
numero = int(input("digite o numero para tabuada: "))


#chamando a função
#enviando parametros 
tabuada(numero)