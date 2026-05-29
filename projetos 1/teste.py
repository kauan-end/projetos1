import random

if escolha=="2":
        print("Modalidade escolhida:Humano vs Maquina")
        jogador=input("pedra, papel ou tesoura")
        
        opcoes = ["pedra", "papel", "tesoura"]

        maquina = random.choice(opcoes)

        print(maquina)