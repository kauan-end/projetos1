while True:
    print("\n=== CALCULADORA ===")

    print("1 soma")
    print("2 subtracao")
    print("3  divisao")
    print("4 multiplicaçao")
    print("5 sair ")

    opcao=input("Escolha uma opcao") 

    if opcao == "0":
        print("encerrar progama!")
        break

    elif opcao in ("1,2,3,4"):
         num1 = float(input("Digite o primeiro número: "))
         num2 = float(input("Digite o segundo número: "))

         if opcao== "1":
             resultado==num1 + num2
             print("resultado",resultado)
         
         elif opcao== "2":
             resultado==num1 - num2
             print("resultado",resultado)

         elif opcao== "3":
             if opcao==0:
                print("Erro: divisão por zero não é permitida!")

             else:
                resultado = num1 / num2
                print("Resultado:", resultado)
        

    else:
     print("Opção inválida! Tente novamente.")


#/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/     
                 
#6.1 facil
while True:

    print("\n=== CALCULADORA POR EXPRESSÃO ===")
    print("Formato: numero operador numero (ex: 10 + 5)")
    print("Digite 'sair' para encerrar")

    entrada=input(">> ")

    if entrada.lower()=="sair":
        print("encerrar calculadora!")
        break

    partes = entrada.split()

    if len(partes) != 3:
        print("Erro: formato inválido!")

    else:
        num1 = float(partes[0])
        operador = partes[1]
        num2 = float(partes[2])

    if operador=="+":
         print("Resultado:", num1 + num2)

    elif   operador=="-":
         print("Resultado:", num1 - num2)   

    elif  operador=="*":
         print("Resultado:", num1 * num2)

    elif operador == "/":
      if num2 == 0:
        print("Erro: divisão por zero não é permitida!")
      else:
         print("Resultado:", num1 / num2)

    else:
       print("Erro: operador inválido!")

#/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/

#6.1 medio

while True:

    print("\n=== CALCULADORA ===")
    print("Ex: 2 + 3 * 4")
    print("Digite 'sair' para encerrar")

    entrada = input(">> ")

    if entrada == "sair":
        print("Encerrando...")
        break

    i = 0
    numero = ""
    resultado = 0
    operador = "+"
    erro = False

    while i < len(entrada):

        c = entrada[i]

        if c != " " and c != "+" and c != "-" and c != "*" and c != "/":
            numero = numero + c

        else:
            if numero == "":
                if c != " ":
                    print("Erro: formato inválido!")
                    erro = True
                    break
            else:
                num = float(numero)

                if operador == "+":
                    resultado = resultado + num
                elif operador == "-":
                    resultado = resultado - num
                elif operador == "*":
                    resultado = resultado * num
                elif operador == "/":
                    if num == 0:
                        print("Erro: divisão por zero!")
                        erro = True
                        break
                    resultado = resultado / num

                numero = ""

            if c == "+" or c == "-" or c == "*" or c == "/":
                operador = c

        i += 1

    if not erro:
        if numero != "":
            num = float(numero)

            if operador == "+":
                resultado = resultado + num
            elif operador == "-":
                resultado = resultado - num
            elif operador == "*":
                resultado = resultado * num
            elif operador == "/":
                if num == 0:
                    print("Erro: divisão por zero!")
                    continue
                resultado = resultado / num

            print("Resultado:", resultado)
        else:
            print("Erro: expressão inválida!")


   

             

  



   

    
