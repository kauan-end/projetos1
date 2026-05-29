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


contador=1
jogadorpontos1=0
jogadorpontos2=0
pedra=1
papel=2
tesoura=3

while contador==1:
        escolha=input(f"{nome} qual modalidade gostaria de jogar? (1,2 OU 3) ").format()
        
        if escolha=="1": 
            print("Modalidade escolhida: Humano vs Humano")
            print("1=pedra")
            print("2=papel")
            print("3=tesoura")
    
            jogador1=int(input("jogador1 digite sua escolha: "))
            jogador2=int(input("jogador2 digite sua escolha: "))

            if jogador1!=1 and jogador1!=2 and jogador1!=3:#verifica o imput do jogador1(1,2,3)
                print("INVALIDO!")
                break
            if jogador2!=1 and jogador2!=2 and jogador2!=3:#verifica o imput do jogador2(1,2,3)
                print("INVALIDO!")
                break

            if jogador1==jogador2:
                print("EMPATE!")
            elif jogador1==1 and jogador2==3:
                print("jogador1 venceu")
                jogadorpontos1+=1
            elif jogador1==2 and jogador2==1:
                print("jogaodrq venceu")
                jogadorpontos1+=1
            elif jogador1==3 and jogador2==2:
                print("jogador1 venceu")
                jogadorpontos1+=1
            else:
                print("jogador2 venceu")
                jogadorpontos2+=1

        print("1 para continuar e 0 para sair:")   
        continuar=int(input(" "))
        
        if continuar==0:
            break
#placar do modo
print("placar")
print(jogadorpontos1)
print(jogadorpontos2)

escolha=input(f"{nome} qual modalidade gostaria de jogar? (1,2 OU 3) ").format()




import random

#variaveis
continuar=1
jogadorpontos=0
maquinapontos=0
pedra=1
papel=2
tesoura=3
#lupin infinito
while continuar==1:
    
    if escolha=="2":
        print("humano vs maquina")
        print("1=pedra")
        print("2=papel")
        print("3=tesoura")
    

        jogador=int(input("digite sua escolha:"))#escolha do jogador

        if jogador!=1 and jogador!=2 and jogador!=3:#verifica o imput do jogador(1,2,3)
            print("INVALIDO!")
            break

        maquina=random.randint(1,3)#escolhe uym numero aleatoriamente entre 1 e 3

        if jogador==maquina:#todos os ifs são as condições q o jogador ganha
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

        else:# se as condições não forem compridas a maquina ganha
            print("maquina ganhou")
            maquinapontos+=1

    #condição para continuar ou sair do progama
        print("1 para continuar e 0 para sair:")   
        continuar=int(input(" "))
        
        if continuar==0:
         break
#placar do modo
print("placar")
print(jogadorpontos)
print(maquinapontos)














