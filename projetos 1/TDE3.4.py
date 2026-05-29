usuario = input("Digite seu usuario: ")
senha = input("Digite sua senha: ")

if usuario == "admin" and senha == "1234":
    print("Acesso concedido")

elif usuario == "convidado" and senha == "":
    print("Acesso restrito")

else:
    print("Acesso bloqueado")

