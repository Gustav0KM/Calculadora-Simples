expressao = input("Digite a expressão matemática (Ex: 3 + 4): ")
    
try:
        resultado = eval(expressao)
        print("Resultado", resultado)
except Exception as e:
        print("Erro! Utilize '+', '-', '*'(multiplicação), '/'(divisão)!")