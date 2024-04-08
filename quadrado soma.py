def quadrado_soma(valores):
    soma = sum(valores)
    quadrado = soma ** 2
    return quadrado


valores = []
for i in range(3):
    valor = int(input(f'Digite o {i+1}º valor inteiro: '))
    valores.append(valor)

resultado = quadrado_soma(valores)

print(f'O quadrado da soma dos valores é: {resultado}')