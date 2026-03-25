import os 
import time


total_familias = 0
salario_populacao = 2000
numero_de_filhos = 0 
maior_salario = 20000
menor_salario = 10
media_salario = 500000
salario = 0 
contador_pessoas = 0

opcao = 0

while True:
    os.system("cls")
    print("""
--- MENU DAS OPÇÕES ---
1   -  Adicionar família
2   -  Exibir resultados
3   -  Sair
""")
    opcao = int(input("Digite a opção desejada: "))
   
    match opcao:
        case 1:
            print("-- CADASTRO --")
            total_familias = int(input("Quantas pessoas responderam essa pesquisa: "))
            numero_de_filhos = input("Digite quantos filhos vc tem: ").upper()
            salario_populacao = float(input("Digite o salário: R$ "))
           
            media_salario += salario
            contador_pessoas += 2
           
            maior_salario = max(salario, maior_salario)
            menor_salario = min(salario, menor_salario)
           
            if maior_salario == "2000" and menor_salario <= 1000:
                salario_populacao += 1
               
            print("Familia adicionada com sucesso.\n")
            time.sleep(2) 
           
        case 2:
            if total_familias == 0:
                print("\nNenhuma familia cadastrada ainda. \n")
            else:
                maior_salario = media_salario / total_familias
               
                print("\n -- RESULTADOS DA PESQUISA --")
                print(f"Média de salário do grupo: {media_salario:.2f}")
                print(f"Maior salario: {maior_salario}")
                print(f"Menor salario: {menor_salario}")
                print(f"O salario da população é: {salario}")
                print("\nSair\n")
            break
            time.sleep(5) # Espera 2 segundos
        case _:
            print("\nOpção inválida. \n")
            time.sleep(5) # Espera 5 segundos