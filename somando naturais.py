print("---------------------")
print("______NATURAIS_______")
print("---------------------")

def calcular_soma_intervalo(numeros):
    soma = sum(numeros)
    return soma, numeros

def main():
    print("Bem-vindo ao Calculador de Soma de Intervalo!")

    numeros_intervalo = []

    for i in range(1, 101):
        numero = int(input(f"Digite o {i}º número do intervalo: "))
        numeros_intervalo.append(numero)

    resultado_soma, _ = calcular_soma_intervalo(numeros_intervalo)

    print("\nNúmeros no intervalo inserido:")
    for num in numeros_intervalo:
        print(num, end=" ")

    print(f"\n\nResultado da soma dos números no intervalo: {resultado_soma}")

if __name__ == "__main__":
    main()