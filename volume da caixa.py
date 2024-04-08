print("---------------------")
print("_________VOLUME______")
print("---------------------")


def calcular_volume(comprimento, largura, altura):
    volume = comprimento * largura * altura
    return volume

comprimento = float(input('Digite o comprimento da caixa (em metros): '))
largura = float(input('Digite a largura da caixa (em metros): '))
altura = float(input('Digite a altura da caixa (em metros): '))

volume_calculado = calcular_volume(comprimento, largura, altura)

print(f'O volume da caixa é: {volume_calculado} metros cúbicos')