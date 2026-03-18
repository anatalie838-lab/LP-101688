import os 

os.system("cls")

print("menu")
print("""
      ======================================================MENU=================================================================
      CODIGO      PRATO      PREÇO 
      1           PICANHA    R$25,00
      2           LASANHA    R$20,00
      3           STROGONOFF R$18,00
      3           BIFE ACEBOLADO R$ 15,00
      5           PÃO COM OVO R$5,00
""")
codigo = int(input("digite o codigo do prato escolhido: "))
match codigo:
        case 1: 
            print("picanha | R$25,00")
        case 2: 
             print("lasanha | R$20,00")
        case 3: 
            print("strogonoff | R$18,00")
        case 4:
            print("bife acebolado | R$15:00")
        case 5:
            print("pao com ovo | R$5,00")
        case _:
            print("escolha um dos codigos a cima")

print("==============VALEU=================")