#Exercício 1
import random

lista = []

for i in range(10):
    numero = random.randint(1, 100)
    lista.append(numero)

print(lista)

#Exercício 2
lista = []

for i in range(3):
    numero = int(input("Digite um número: "))
    lista.append(numero)

print(lista)

#Exercício 3
frase = input("Digite uma frase: ")

lista = frase.split()

print(lista)

#Exercício 4
lista = []

for i in range(1, 11):
    lista.append(i)

lista.reverse()

print(lista)

#Exercício 5
palavras = ["casa", "computador", "sol", "python", "universidade"]

maior = max(palavras, key=len)
menor = min(palavras, key=len)

print("Palavra mais longa:", maior)
print("Palavra mais curta:", menor)

#Exercício 6
pares = []
impares = []

for i in range(1, 11):
    if i % 2 == 0:
        pares.append(i)
    else:
        impares.append(i)

terceira_lista = pares + impares

print(terceira_lista)

#Exercício 7
lista = []

for i in range(1, 101):
    lista.append(i)

print("Números pares:")

for numero in lista:
    if numero % 2 == 0:
        print(numero)

#Exercício 8
lista = []

for i in range(1, 11):
    lista.append(i ** 2)

soma = sum(lista)

print("Lista:", lista)
print("Soma:", soma)

#Exercício 9
import random
import string

alfabeto = list(string.ascii_lowercase)

random.shuffle(alfabeto)

print(alfabeto)

letra = input("Digite uma letra: ")

posicao = int(input("Digite a posição que você acha que a letra está: "))

if alfabeto[posicao] == letra:
    print("Acertou!")
else:
    print("Errou!")
    print("A letra estava na posição:", alfabeto.index(letra))

#Exercício 10 — Jogo da Velha
tabuleiro = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

jogador = "X"

for rodada in range(9):

    print("\nTabuleiro:")
    
    for linha in tabuleiro:
        print(linha)

    linha = int(input("Digite a linha (0-2): "))
    coluna = int(input("Digite a coluna (0-2): "))

    if tabuleiro[linha][coluna] == " ":
        tabuleiro[linha][coluna] = jogador

        # Troca jogador
        if jogador == "X":
            jogador = "O"
        else:
            jogador = "X"

    else:
        print("Posição ocupada!")

print("\nTabuleiro final:")

for linha in tabuleiro:
    print(linha)