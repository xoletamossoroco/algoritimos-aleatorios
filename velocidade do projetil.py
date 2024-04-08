print("---------------------")
print("______VELOCIDADE_____")
print("---------------------")


def calcular_velocidade(distancia_km, tempo_min):
    distancia_metros = distancia_km * 1000
    tempo_segundos = tempo_min * 60

    velocidade = distancia_metros / tempo_segundos

    return velocidade


print("Bem-vindo ao Calculador de Velocidade de Projéteis!")
print("Por favor, informe os seguintes dados:")

distancia_km = float(input('Distância percorrida pelo projétil (em quilômetros): '))
tempo_min = float(input('Tempo que o projétil levou para percorrer (em minutos): '))

velocidade_ms = calcular_velocidade(distancia_km, tempo_min)

print(f'\nA velocidade do projétil é de {velocidade_ms:.2f} metros por segundo.')