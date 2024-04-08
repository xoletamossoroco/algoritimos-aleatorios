print("---------------------")
print("______CONVERSÃO______")
print("---------------------")

def converter_dolar_para_real(valor_dolar, cotacao_dolar):
    valor_real = valor_dolar * cotacao_dolar
    return valor_real

cotacao_dolar = float(input('Qual é a cotação do dólar em reais? R$ '))
valor_dolar = float(input('Quanto em dólares você deseja converter para reais? US$ '))

valor_convertido = converter_dolar_para_real(valor_dolar, cotacao_dolar)

print(f'O valor em reais é: R$ {valor_convertido:.2f}')