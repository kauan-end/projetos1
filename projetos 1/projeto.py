ano_nascimento = int(input("Digite seu ano de nascimento: "))
ano_atual = 2026

idade = ano_atual - ano_nascimento

print("Sua idade é:", idade)


2 #Calcular valor do aluguel do carro
dias = int(input("Quantos dias o carro foi alugado? "))
valor_por_dia = 100

total = dias * valor_por_dia

print("Valor total a pagar: R$", total)


3 #Converter Celsius para Fahrenheit
celsius = float(input("Digite a temperatura em Celsius: "))

fahrenheit = (celsius * 9/5) + 32

print("Temperatura em Fahrenheit:", fahrenheit)

4 #Calcular média de 4 notas
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
nota4 = float(input("Digite a quarta nota: "))

media = (nota1 + nota2 + nota3 + nota4) / 4

print("A média é:", media)

5 #Calcular idade em meses
idade = int(input("Digite sua idade em anos: "))

meses = idade * 12

print("Sua idade em meses é:", meses)

6 #Calcular preço de venda por quilo
preco_quilo = float(input("Digite o preço do quilo: "))
peso = float(input("Digite o peso do produto em kg: "))

total = preco_quilo * peso

print("Valor total a pagar: R$", total)