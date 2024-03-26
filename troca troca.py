def trocar_valores(a, b):

    print(f'Valores iniciais: A = {a}, B = {b}')
    a, b = b, a

    print(f'Valores após troca: A = {a}, B = {b}')

valor_a = int(input("Digite o valor para A: "))

valor_b = int(input("Digite o valor para B: "))

trocar_valores(valor_a, valor_b)