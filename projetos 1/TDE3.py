# Exercicio da Floresta.
print("Você está em uma floresta.")
caminho = input("Escolha um caminho (esquerda/direita): ").lower()

if caminho== "esquerda":
    print("voce encontrou um rio:")
    açao=input("Deseja atravessar ou voltar:").lower()

    if açao == "atravessar":
        print("Você chega a uma vila segura!")
    elif açao == "voltar":
        print("Você permanece perdido na floresta.")
    else:
        print("Opçao invalida")  

if caminho=="direita":
    print("voce encontrou uma montanha:") 
    açao=input("deseja subir ou voltar").lower()

    if açao == "subir":
        print("Voce encontrou um tesouro!")    
    elif açao == "voltar":
        print("Voce permanece perdido na floresta!") 
    else: 
        print("opçao invalida") 

        

