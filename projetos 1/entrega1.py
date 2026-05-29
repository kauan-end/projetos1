while True:
    try:
        nota = float(input("Digite a nota do aluno (0 a 10): "))
        
        if 0 <= nota <= 10:
            print(f"Nota válida: {nota}")
            break
        else:
            print("Nota inválida! A nota deve estar entre 0 e 10.")
    
    except ValueError:
        print("Entrada inválida! Digite um número.")