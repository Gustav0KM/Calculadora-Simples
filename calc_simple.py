while True:
    print("""Escolha uma opção: 
      1. Adição
      2. Subtração
      3. Multiplicação
      4. Divisão
      5. Limpar
      """)

    escolha = input('->')
    
    if escolha == '5':
        break

    num1 = input("Digite o primeiro número: ")
    num2 = input("Digite o segundo número: ")

    if escolha == '1':
        print(f"{num1} + {num2} = {int(num1) + int(num2)}\n") 
   
    if escolha == '2':
        print(f"{num1} - {num2} = {int(num1) - int(num2)}\n")
    
    if escolha == '3':
        print(f"{num1} x {num2} = {int(num1) * int(num2)}\n")
    
    if escolha == '4':
        print(f"{num1} / {num2} = {int(num1) / int(num2)}\n")

