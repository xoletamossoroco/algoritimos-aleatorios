print("---------------------")
print("_________SOMA________")
print("---------------------")

def soma_quadrados(valores):
    soma = sum(valor ** 2 for valor in valores)
    return soma

print("Bem-vindo à Calculadora de Soma dos Quadrados!")
print("Por favor, digite três valores inteiros:")

valores = []
for i in range(3):
    valor = int(input(f'Digite o {i+1}º valor inteiro: '))
    valores.append(valor)

resultado = soma_quadrados(valores)

print(f'\nA soma dos quadrados dos valores é: {resultado}')