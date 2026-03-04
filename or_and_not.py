import os 

os.system("cls")

login_usuario= "amandona linda"
senha_usuario= 20102006

login=input("Insira seu login: ")
senha=int(input("Insira sua senha: "))

if login == login_usuario and senha == senha_usuario:
    print("usuario nao cadastrado ")
else: 
    print("usuario não cadastrado")
