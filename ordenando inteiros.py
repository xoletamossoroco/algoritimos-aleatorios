print("---------------------")
print("_______INTEIRO_______")
print("---------------------")

def ordenar_decrescente(array):
    return sorted(array, reverse=True)

def main():
    elementos = []

    print("=== Ordenando Elementos em Ordem Decrescente ===")
    print("Por favor, digite 12 números inteiros:")

    for i in range(1, 13):
        elemento = int(input(f"Digite o {i}º número inteiro: "))
        elementos.append(elemento)

    elementos_ordenados = ordenar_decrescente(elementos)

    print("\nElementos ordenados em ordem decrescente:")
    for elemento in elementos_ordenados:
        print(elemento, end=" ")

if __name__ == "__main__":
    main()