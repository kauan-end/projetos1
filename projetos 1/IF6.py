import math


lados=int(input("DIGITE O NUMERO DE LADOS:"))
medida = float(input("Digite a medida do lado (cm): "))

if lados == 3:
    area = (math.sqrt(3) / 4) * (medida ** 2)
    print("TRIÂNGULO")
    print(f"Área: {area:.2f} cm²")

elif lados== 4:
    area= medida**2
    print("QUADRADO")
    print(f"Área: {area:.2f} cm²")

elif lados==5:
    print("pentagono") 


else:
    print("Polígono não identificado")       