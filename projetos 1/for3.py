
numero = int(input("Digite um numero inteiro n: "))

soma = 0
ex = " "

for i in range(1, numero + 1):
    soma += i
    if i == 1:
        ex += str(i)
    else:
        ex += "+" + str(i)

print(ex + "=" + str(soma))       


    
    

