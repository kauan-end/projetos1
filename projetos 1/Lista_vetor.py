#Exercício 1
A = [1, 0, 5, -2, -5, 7]

soma = A[0] + A[1] + A[5]

print("Soma:", soma)

A[4] = 100

for i in range(6):
    print(A[i])

#Exercício 2
vetor = []

for i in range(6):
    valor = int(input("Digite um valor: "))
    vetor.append(valor)

print("Valores lidos:")

for i in range(6):
    print(vetor[i])

#Exercício 3
vetor = []
quadrado = []

for i in range(10):
    numero = float(input("Digite um número: "))
    vetor.append(numero)
    quadrado.append(numero ** 2)

print("Vetor original:")
for i in range(10):
    print(vetor[i])

print("Vetor ao quadrado:")
for i in range(10):
    print(quadrado[i])

#Exercício 4
vetor = []

for i in range(8):
    numero = int(input("Digite um número: "))
    vetor.append(numero)

X = int(input("Digite a posição X: "))
Y = int(input("Digite a posição Y: "))

soma = vetor[X] + vetor[Y]

print("Soma:", soma)

#Exercício 5
vetor = []
pares = 0

for i in range(10):
    numero = int(input("Digite um número: "))
    vetor.append(numero)

    if numero % 2 == 0:
        pares += 1

print("Quantidade de pares:", pares)

#Exercício 6
vetor = []

for i in range(10):
    numero = int(input("Digite um número: "))
    vetor.append(numero)

maior = max(vetor)
menor = min(vetor)

print("Maior valor:", maior)
print("Menor valor:", menor)

#Exercício 7
vetor = []

for i in range(10):
    numero = int(input("Digite um número: "))
    vetor.append(numero)

maior = vetor[0]
posicao = 0

for i in range(10):
    if vetor[i] > maior:
        maior = vetor[i]
        posicao = i

print("Vetor:")
for i in range(10):
    print(vetor[i])

print("Maior valor:", maior)
print("Posição:", posicao)

#Exercício 8
notas = []
soma = 0

for i in range(15):
    nota = float(input("Digite a nota do aluno: "))
    notas.append(nota)
    soma += nota

media = soma / 15

print("Média geral:", media)

#Exercício 9
vetor = []
negativos = 0
soma_positivos = 0

for i in range(10):
    numero = float(input("Digite um número: "))
    vetor.append(numero)

    if numero < 0:
        negativos += 1
    else:
        soma_positivos += numero

print("Quantidade de negativos:", negativos)
print("Soma dos positivos:", soma_positivos)

#Exercício 10
valores = []
soma = 0

for i in range(5):
    numero = float(input("Digite um valor: "))
    valores.append(numero)
    soma += numero

maior = max(valores)
menor = min(valores)
media = soma / 5

print("Valores lidos:")
for i in range(5):
    print(valores[i])

print("Maior valor:", maior)
print("Menor valor:", menor)
print("Média:", media)

#Exercício 11
valores = []

for i in range(5):
    numero = float(input("Digite um valor: "))
    valores.append(numero)

maior = max(valores)
menor = min(valores)

pos_maior = valores.index(maior)
pos_menor = valores.index(menor)

print("Maior valor:", maior)
print("Posição do maior:", pos_maior)

print("Menor valor:", menor)
print("Posição do menor:", pos_menor)