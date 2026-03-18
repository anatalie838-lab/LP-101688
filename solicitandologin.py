import os 
os.system ("cls")
#refaz
login_correto: input("Amanda" )
senha_correta: "12345"
QUANTIDADE_DE_VEZES: 3

for i in range (QUANTIDADE_DE_VEZES):

    while True:
        login = input("digite seu login: ")
        enha = input("digiste sua senha: ")

        login_esta_correto = login == login_correto
        senha_esta_correta = senha == senha_correta
        if login_esta_correto and senha_esta_correta:
            print("bem vindo ao sistema! ")
        break
    else: 
     print("login esta invalido. ")
     print("tente novamente...")

