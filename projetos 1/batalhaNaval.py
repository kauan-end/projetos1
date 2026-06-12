import random


linhas = 5
colunas = 10
total_navios = 5
letras = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]


def menu():
    print("""
╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║  ██████╗  █████╗ ████████╗ █████╗ ██╗     ██╗  ██╗ █████╗    ║
║  ██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗██║     ██║  ██║██╔══██╗   ║
║  ██████╔╝███████║   ██║   ███████║██║     ███████║███████║   ║
║  ██╔══██╗██╔══██║   ██║   ██╔══██║██║     ██╔══██║██╔══██║   ║
║  ██████╔╝██║  ██║   ██║   ██║  ██║███████╗██║  ██║██║  ██║   ║
║  ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝   ║
║                                                              ║
║   ███╗   ██╗ █████╗ ██╗   ██╗ █████╗ ██╗                     ║
║   ████╗  ██║██╔══██╗██║   ██║██╔══██╗██║                     ║
║   ██╔██╗ ██║███████║██║   ██║███████║██║                     ║
║   ██║╚██╗██║██╔══██║╚██╗ ██╔╝██╔══██║██║                     ║
║   ██║ ╚████║██║  ██║ ╚████╔╝ ██║  ██║███████╗                ║
║   ╚═╝  ╚═══╝╚═╝  ╚═╝  ╚═══╝  ╚═╝  ╚═╝╚══════╝                ║
║                                                              ║
║            ⚓ A GUERRA DOS OCEANOS ⚓                        ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
""")
    print("1 - Jogar")
    print("2 - Regras")
    print("3 - Sair")
    print("+++++++++++++++++++++++++++")


def regras():
    print("++++++++++++++++++++++++++")
    print("📜 REGRAS:")
    print("- Voce tem 5 navios 🚢")
    print("- Acerto = X 💥")
    print("- Erro = O 🌊")
    print("- Destrua todos os navios pra ganhar 🏆")
    print("++++++++++++++++++++++++++")

def criaTabuleiro():
    tabuleiro = []
    for i in range(linhas):
        linha = []
        for x in range(colunas):
            linha.append(".")
        tabuleiro.append(linha)
    return tabuleiro


def exibirTabuleiro(tabuleiro, nome):
    print(nome)
    simbolos = {
        ".": "🌊",
        "O": "❌",
        "X": "💥",
        "N": "🚢"
    }
    cabecalho = "    "

    for letra in letras:
        cabecalho = cabecalho + letra + "  "

    print(cabecalho)

    for linha in range(linhas):
        texto = str(linha) + "   "

        for coluna in range(colunas):
             valor = tabuleiro[linha][coluna]

             if valor in simbolos:
                texto = texto + str(simbolos[valor]) + " "
             else:
                texto = texto + str(valor) + " "

        print(texto)
     

def lerlinha():
    validos = ["0", "1", "2", "3", "4"]
    while True:
        n = input("Linha (0-4): ")
        if n not in validos:
            print(" Digite um numero valido entre 0 e 4!")
        else:
            return int(n)
            
def NaviosJogador(tabuleiro):
    navios=0
    while navios < total_navios:
        print(f"\nPosicionando navio {navios + 1} de {total_navios}")
       
        linha = lerlinha()
        coluna =  input("Coluna (A-J): ").upper()
        if coluna not in letras:
                print(" Coluna invalida!")
                continue
        col = letras.index(coluna) 
            
        if linha < 0 or linha >= linhas:
            print("Linha inválida!")
            continue
        if tabuleiro[linha][col] != '.':
            print("Já tem navio!")
            continue
        tabuleiro[linha][col] = "N"
        navios += 1

def NaviosComputador(tabuleiro):
    navios=0
    while navios < total_navios:
        linha = random.randint(0, linhas - 1)
        coluna = random.randint(0, colunas - 1)
        if tabuleiro[linha][coluna] == "N":
            continue
        tabuleiro[linha][coluna] = "N"
        navios += 1

def ataqueJogador(RealPC, ExibicaoPC, ExibicaoJogador):
    linha = lerlinha()
    coluna = input("Coluna (A-J): ").upper()
    if coluna not in letras:
        print("Coluna invalida!")
        return None, None, None
    col = letras.index(coluna)
    if linha < 0 or linha >= linhas:
        print("Linha inválida!")
        return None, None, None

    if ExibicaoPC[linha][col] == 'X' or ExibicaoPC[linha][col] == 'O':
        print("Você já atacou essa posição!")
        return None, None, None
    if RealPC[linha][col] == "N":
        ExibicaoPC[linha][col] = 'X'
        RealPC[linha][col] = '.'
        return True, linha, col
    else:
        ExibicaoPC[linha][col] = 'O'
        return False, linha, col
    
def ataqueComputador(RealJogador, ExibicaoJogador):
    while True:
        linha = random.randint(0, linhas - 1)
        coluna = random.randint(0, colunas - 1)
        if ExibicaoJogador[linha][coluna] == 'X' or ExibicaoJogador[linha][coluna] == 'O':
            continue
        if RealJogador[linha][coluna] == "N":
            RealJogador[linha][coluna] = '.'
            ExibicaoJogador[linha][coluna] = 'X'
            return True, linha, coluna
        else:
            ExibicaoJogador[linha][coluna] = 'O'
            return False, linha, coluna
        
def contarNavios(tabuleiro):
    count = 0
    for linha in tabuleiro:
        count += linha.count("N")
    return count

def jogar():
    tabuleiroJogador = criaTabuleiro()
    tabuleiroComputador = criaTabuleiro()
    tabuleiroExibicaoComputador = criaTabuleiro()
    tabuleiroExibicaoJogador = criaTabuleiro()

    NaviosJogador(tabuleiroJogador)
    for i in range(linhas):
        for j in range(colunas):
            if tabuleiroJogador[i][j] == "N":
                tabuleiroExibicaoJogador[i][j] = "N"

    NaviosComputador(tabuleiroComputador)

    while True:
        print("\n========================================")
       
        print("escolha onde atacar")
        exibirTabuleiro(tabuleiroExibicaoComputador, "Tabuleiro do Computador")
        print("Embarcações restantes do computador:", contarNavios(tabuleiroComputador))
        print()
        exibirTabuleiro(tabuleiroExibicaoJogador, "Seu Tabuleiro")
        print("Suas embarcações restantes:", contarNavios(tabuleiroJogador))

        while True:
            acertouJ, linhaJ, colJ = ataqueJogador(tabuleiroComputador, tabuleiroExibicaoComputador, tabuleiroExibicaoJogador)
            if acertouJ is not None:
                break

      
        acertouPC, linhaPC, colPC = ataqueComputador(tabuleiroJogador, tabuleiroExibicaoJogador)

       
        print("\n========================================")
        print("RESULTADO DA RODADA:")

        print("Você atacou:", linhaJ, letras[colJ])

        if acertouJ:
            print("💥 Você acertou!")
        else:
            print("🌊 Você errou!")

        print()

        print("Computador atacou:", linhaPC, letras[colPC])

        if acertouPC:
            print("💥 Computador acertou!")
        else:
            print("🌊 Computador errou!")

        print()
        exibirTabuleiro(tabuleiroExibicaoComputador, "Tabuleiro do Computador (seus ataques)")
        print("Embarcações restantes do computador:", contarNavios(tabuleiroComputador))
        print()
        exibirTabuleiro(tabuleiroExibicaoJogador, "Seu Tabuleiro (ataques do computador)")
        print("Suas embarcações restantes:", contarNavios(tabuleiroJogador))
        if contarNavios(tabuleiroComputador) == 0 and contarNavios(tabuleiroJogador) == 0:
            print("Empate!")
            break
        elif contarNavios(tabuleiroComputador) == 0:
            print("Você ganhou!")
            print("""
╔════════════════════════════════════════════════════════════════════╗
║                                                                    ║
║                     ⚓ BATALHA NAVAL ⚓                            ║
║                                                                    ║
║                          AGRADECIMENTOS                            ║
║                                                                    ║
║                Obrigado por acompanhar nosso projeto!              ║
║                                                                    ║
║                       🚢     🌊     🚢                            ║
║                                                                    ║
║                    Desenvolvido pela equipe:                       ║
║                                                                    ║
║                       ★ Kauan Davids ★                             ║
║                       ★ Thiago Batista ★                           ║
║                       ★ Henrique de Farias ★                       ║
║                                                                    ║
╚════════════════════════════════════════════════════════════════════╝


                          |    |    |
                         )_)  )_)  )_)
                        )___))___))___)\\
                       )____)____)_____)\\\\
                     _____|____|____|____\\\\__
            ---------\\                   /---------
              ^^^^^ ^^^^^^^^^^^^^^^^^^^^^
                ^^^^      ^^^^     ^^^
                     ^^^^      ^^^

            🌊 Obrigado por navegar conosco! 🌊
""")
            break

        elif contarNavios(tabuleiroJogador) == 0:
            print("Computador ganhou!")
            print("""
╔════════════════════════════════════════════════════════════════════╗
║                                                                    ║
║                     ⚓ BATALHA NAVAL ⚓                            ║
║                                                                    ║
║                          AGRADECIMENTOS                            ║
║                                                                    ║
║                Obrigado por acompanhar nosso projeto!              ║
║                                                                    ║
║                       🚢     🌊     🚢                            ║
║                                                                    ║
║                    Desenvolvido pela equipe:                       ║
║                                                                    ║
║                       ★ Kauan Davids ★                             ║
║                       ★ Thiago Batista ★                           ║
║                       ★ Henrique de Farias ★                       ║
║                                                                    ║
╚════════════════════════════════════════════════════════════════════╝


                          |    |    |
                         )_)  )_)  )_)
                        )___))___))___)\\
                       )____)____)_____)\\\\
                     _____|____|____|____\\\\__
            ---------\\                   /---------
              ^^^^^ ^^^^^^^^^^^^^^^^^^^^^
                ^^^^      ^^^^     ^^^
                     ^^^^      ^^^

            🌊 Obrigado por navegar conosco! 🌊
""")
            break

while True:
    menu()
    opp = input("Escolha uma opção: ")
    if opp == "1":
        jogar()
        break
    elif opp == "2":
        regras()
        input("Pressione Enter para voltar ao menu:")
    elif opp == "3":
        print("Até a próxima!")
        exit()
    else:
        print("Opção inválida!")