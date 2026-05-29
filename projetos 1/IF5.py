altura=float(input("Digite sua altura:"))
sexo=int(input("Digite seu sexo,1 para feiminino/2 para masculino:"))

if sexo==1:
    peso_ideal= (62.1*altura)-44.7

elif sexo==2:
    peso_ideal= (72.7*altura)-58

else:
    print("sexo invalido!")  
    exit()      

print (f"seu peso ideal é: {peso_ideal:.2f}kg")   
