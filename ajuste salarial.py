def calcular_novo_salario(salario_atual, percentual_reajuste):
    reajuste = salario_atual * (percentual_reajuste / 100)

    novo_salario = salario_atual + reajuste

    return novo_salario

salario_atual = float(input("Digite o valor do salário mínimo atual: R$ "))
percentual_reajuste = float(input("Digite o percentual de reajuste (%): "))

novo_salario =calcular_novo_salario(salario_atual, percentual_reajuste)

print(f'O novo salário após o reajuste de {percentual_reajuste}% é: R$ {novo_salario:.2f}')