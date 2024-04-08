print("---------------------")
print("_______VOTAÇÃO_______")
print("---------------------")

def calcular_percentual(valor, total):
    if total == 0:
        return 0
    else:
        return (valor / total) * 100

print("Por favor, informe a quantidade de votos para cada candidato, votos nulos e votos em branco:")
votos_validos_a = int(input('Votos válidos para o candidato A: '))
votos_validos_b = int(input('Votos válidos para o candidato B: '))
votos_validos_c = int(input('Votos válidos para o candidato C: '))
votos_nulos = int(input('Votos nulos: '))
votos_branco = int(input('Votos em branco: '))

total_eleitores = votos_validos_a + votos_validos_b + votos_validos_c + votos_nulos + votos_branco

percentual_validos = calcular_percentual(votos_validos_a + votos_validos_b + votos_validos_c, total_eleitores)
percentual_validos_a = calcular_percentual(votos_validos_a, total_eleitores)
percentual_validos_b = calcular_percentual(votos_validos_b, total_eleitores)
percentual_validos_c = calcular_percentual(votos_validos_c, total_eleitores)
percentual_nulos = calcular_percentual(votos_nulos, total_eleitores)
percentual_branco = calcular_percentual(votos_branco, total_eleitores)

print('\nResultados da Eleição:')
print(f'Número total de eleitores: {total_eleitores}')
print(f'Percentual de votos válidos: {percentual_validos:.2f}%')
print(f'Percentual de votos válidos para o candidato A: {percentual_validos_a:.2f}%')
print(f'Percentual de votos válidos para o candidato B: {percentual_validos_b:.2f}%')
print(f'Percentual de votos válidos para o candidato C: {percentual_validos_c:.2f}%')
print(f'Percentual de votos nulos: {percentual_nulos:.2f}%')
print(f'Percentual de votos em branco: {percentual_branco:.2f}%')