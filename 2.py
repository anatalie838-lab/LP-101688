import os 

os.system("cls")

def metros_para_centimetros(metros):
    return metros * 100
valor = float(input("digite o valor em metros: "))
resultado = metros_para_centimetros(valor)
print(f"o valor de centimetros é {resultado} cm")