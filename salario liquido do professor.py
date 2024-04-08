print("---------------------")
print("______PROFESSOR______")
print("---------------------")


def calcular_salario(horas_trabalhadas, valor_hora_aula, percentual_desconto):
    salario_bruto = horas_trabalhadas * valor_hora_aula

    desconto = salario_bruto * (percentual_desconto / 100)

    salario_liquido = salario_bruto - desconto

    return salario_bruto, salario_liquido


print("Bem-vindo ao Calculador de Salário!")
print("Por favor, forneça as seguintes informações:")

horas_trabalhadas = float(input('Número de horas trabalhadas no mês: '))
valor_hora_aula = float(input('Valor da hora-aula: R$ '))
percentual_desconto = float(input('Percentual de desconto do INSS (%): '))

salario_bruto, salario_liquido = calcular_salario(horas_trabalhadas, valor_hora_aula, percentual_desconto)

print(f'\nSalário bruto: R$ {salario_bruto:.2f}')
print(f'Salário líquido: R$ {salario_liquido:.2f}')
