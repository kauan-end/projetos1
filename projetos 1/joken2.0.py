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



