print("---------------------")
print("_______CONVERSÃO_______")
print("---------------------")

def converter_real_para_dolar(valor_real, cotacao_dolar):
    valor_dolar = valor_real / cotacao_dolar
    return valor_dolar

cotacao_dolar = float(input('Qual é a cotação atual do dólar em reais? R$ '))
valor_real = float(input('Quantos reais você deseja converter para dólares? R$ '))

valor_convertido = converter_real_para_dolar(valor_real, cotacao_dolar)

print(f'O valor em dólares é: US$ {valor_convertido:.2f}')