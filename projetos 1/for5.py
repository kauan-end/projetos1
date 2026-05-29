linhas = int(input("Digite a quantidade de linhas: "))

for i in range(1, linhas + 1):
    for x in range(1, i + 1):
        print(x, end="")
    print()