import random

#Apresentação
print("---JOKENPO---")
for i in range(2):
    print("-")

print("As modalidades são: Humano vs Humano, Humano vs Máquina e Máquina vs Máquina")

for i in range(2):
    print("-")

#Nickname e Modos
nome=input("Qual seu nickname? ")

# jogar=input('Você gostaria de jogar? ').format()
# if jogar== "sim" or "s" or "ss" or "gostaria":
#     print('MENU')
#     print('1 -Humano vs Humano')
#     print('2 -Humano vs Máquina')
#     print('3 -Máquina vs Máquina')
# else:
#     print('Resposta inválida, tente novamente')
#     retornar=input("Gostaria de tentar novamente? sim/não: ")
#     if retornar=="sim":
#         print('MENU')
#         print('1 -Humano vs Humano')
#         print('2 -Humano vs Máquina')
#         print('3 -Máquina vs Máquina')
#     else:
#         print("Jogo em suspensão,caso queira tentar novamente reinicie o terminal")

#MECÂNICA DO JOGO
play1="pedra">"tesoura"
play2="tesoura">"papel"
play3="papel">"pedra"

import getpass

contador=1
jogadorpontos1=0
jogadorpontos2=0
pedra=1
papel=2
tesoura=3
escolha=1
opcao=1
continuar="1"

while True:
    continuar="1"
    escolha=input("1.humano vs humano 2.humano contra maquina 3.maquina vc maquina 0.sair: ")

    if escolha=="1":

        while continuar=="1":

            print("Modalidade escolhida: Humano vs Humano")
            print("1=pedra")
            print("2=papel")
            print("3=tesoura")

            jogador1=int(getpass.getpass(prompt=("digite sua escolha")))
            jogador2=int(getpass.getpass(prompt=("digite sua escolha")))

            if jogador1!=1 and jogador1!=2 and jogador1!=3:
                print("INVALIDO!")
                break

            if jogador2!=1 and jogador2!=2 and jogador2!=3:
                print("INVALIDO!")
                break

            if jogador1==jogador2:
                print("EMPATE!")

            elif jogador1==1 and jogador2==3:
                print("jogador1 venceu")
                jogadorpontos1+=1
                

            elif jogador1==2 and jogador2==1:
                print("jogador1 venceu")
                jogadorpontos1+=1

            elif jogador1==3 and jogador2==2:
                print("jogador1 venceu")
                jogadorpontos1+=1

            else:
                print("jogador2 venceu")
                jogadorpontos2+=1

            print("1 para continuar e 0 para sair:")
            continuar=input(" ")

            print(jogador1)
            print(jogador2)

            if continuar=="0":
                print("placar")
                print(jogadorpontos1)
                print(jogadorpontos2)
                break

    continuar="1"
    jogadorpontos=0
    maquinapontos=0
    pedra=1
    papel=2
    tesoura=3

    if escolha=="2":

        while continuar=="1":

            print("humano vs maquina")
            print("1=pedra")
            print("2=papel")
            print("3=tesoura")

            jogador=int(input("digite sua escolha:"))

            if jogador!=1 and jogador!=2 and jogador!=3:
                print("INVALIDO!")
                break

            maquina=random.randint(1,3)

            if jogador==maquina:
                print("empate")

            elif jogador==1 and maquina==3:
                print("jogador ganhou")
                jogadorpontos+=1

            elif jogador==2 and maquina==1:
                print("jogador ganhou")
                jogadorpontos+=1

            elif jogador==3 and maquina==2:
                print("jogador ganhou")
                jogadorpontos+=1

            else:
                print("maquina ganhou")
                maquinapontos+=1

            print("1 para continuar e 0 para sair:")
            continuar=input(" ")

            if continuar=="0":
                print("placar")
                print(jogadorpontos)
                print(maquinapontos)
                break

    elif escolha=="0":
        break

    maquina1pontos=0
    maquina2pontos=0

    if escolha=="3":

        continua="1"

        while continua=="1":

            print("\n--- RODADA INICIADA ---")

            n1 = random.randint(1, 3)
            n2 = random.randint(1, 3)

            if n1 == 1:
                m1 = "pedra"
            elif n1 == 2:
                m1 = "papel"
            else:
                m1 = "tesoura"

            if n2 == 1:
                m2 = "pedra"
            elif n2 == 2:
                m2 = "papel"
            else:
                m2 = "tesoura"

            print("Maquina 1 jogou:", m1)
            print("Maquina 2 jogou:", m2)

            if n1 == n2:
                print(">> RESULTADO: EMPATE!")

            else:

                if n1 == 1:
                    if n2 == 3:
                        print(">> VITORIA DA MAQUINA 1")
                        maquina1pontos+=1
                    else:
                        print(">> VITORIA DA MAQUINA 2")
                        maquina2pontos+=1

                if n1 == 2:
                    if n2 == 1:
                        print(">> VITORIA DA MAQUINA 1")
                        maquina1pontos+=1
                    else:
                        print(">> VITORIA DA MAQUINA 2")
                        maquina2pontos+=1

                if n1 == 3:
                    if n2 == 2:
                        print(">> VITORIA DA MAQUINA 1")
                        maquina1pontos+=1
                    else:
                        print(">> VITORIA DA MAQUINA 2")
                        maquina2pontos+=1

            print("-----------------------")

            continuar = input("1 para continuar / 0 para sair: ")

            if continuar == "0":
                print("\nPLACAR FINAL:")
                print("Maquina 1:", maquina1pontos)
                print("Maquina 2:", maquina2pontos)
                break
                    
            

            

    

    













