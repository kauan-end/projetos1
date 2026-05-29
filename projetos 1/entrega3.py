soma=0
quant=0

while True:
    numero=int(input("Digite um numero:"))

    if numero==-1:
        break

    soma+=quant
    quant+=1

if quant>0:
    media = soma / quant
    print(f"Média dos números: {media}")

else:
    print("Nenhum número válido foi digitado.")
