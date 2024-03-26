print("------------------")
print("  CIRCUNFERENCIA  ")
print("------------------")

pi = 3.14159265

def calcular_area(raio):
    area = pi * (raio ** 2)
    return area

raio = float(input('Digite o raio da ciscunferência: '))

area_calculada = calcular_area(raio)

print('A área da ciscunferência é:', area_calculada)