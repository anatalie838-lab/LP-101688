import os 

os.system("cls")

numero_um = int(input("digite um numero: "))
numero_dois = int(input("digite outro numero: "))

caractere = input("escolha uma operação(+,-,/,*: )")

match caractere:
    case "+":
        soma = numero_um + numero_dois
        print(f"\na soma é: {soma}")
    case "-":
        subtração = numero_um - numero_dois
        print(f"\na subtração é: {subtração}")
    case "/":
        dividir = numero_um / numero_dois
        print(f"\na divisão é: {dividir}") 
    case "*":
        multiplicação = numero_um * numero_dois
        print(f"\na multiplicação é: {multiplicação}")   
        
    case _:     
        print("\noperação invalida! escolha opção disponivel")

print("FIM")       