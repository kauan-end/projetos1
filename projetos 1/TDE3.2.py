numero = int(input("digite um numero:"))

if numero < 0:
    print("OPÇÃO INVÁLIDA")

elif 10 <= numero <= 50:
    print("O numero esta entre 10 e 50!")

elif numero < 10:
    print("o numero e menor que 10!")

else:
    print("o numero e maior que 50!")