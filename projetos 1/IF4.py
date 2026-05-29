valor=int(input("Insira o primeiro valor inteiro:"))
valor1=int(input("Insira o segundo valor inteiro:"))
valor2=int(input("Insira o terceiro valor inteiro:"))

if valor<valor1 and  valor1<valor2:

    if valor1<valor2:
        print(valor,valor1,valor2)

    else:
        print(valor,valor2,valor1)

elif valor1<valor and valor1<valor2:

    if valor<valor2:
        print(valor1,valor,valor2)

    else:
        print(valor1,valor2,valor) 

else:
    if valor<valor1:
     print(valor2,valor,valor1)

    else:
        print(valor2,valor1,valor)