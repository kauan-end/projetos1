maças=float(input("DIgite o numero de maças:"))

if maças<12:
    Preco=0.30

else:
    preco=0.25

total1=maças*preco

print(f"Valor total da compra: R$ {total1:.2f}")        