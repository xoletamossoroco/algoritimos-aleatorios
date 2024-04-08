print("---------------------")
print("___ALGARISMO ROMANO__")
print("---------------------")

def roman_to_int(s):
    valores = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0

    for i in range(len(s)):
        if i > 0 and valores[s[i]] > valores[s[i - 1]]:
            total += valores[s[i]] - 2 * valores[s[i - 1]]
        else:
            total += valores[s[i]]

    return total

def validar_romano(s):
    return all(char in 'IVXLCDM' for char in s)

def main():
    print("Conversor de Numerais Romanos para Inteiros")

    while True:
        numeral_romano = input("Digite um numeral romano ou 'sair' para encerrar: ").upper()

        if numeral_romano == 'SAIR':
            print("Obrigado por usar o conversor. Até logo!")
            break

        if not validar_romano(numeral_romano):
            print("Por favor, digite um numeral romano válido.")
            continue

        resultado = roman_to_int(numeral_romano)
        print(f"O numeral romano '{numeral_romano}' equivale a {resultado} em inteiro.")

if __name__ == "__main__":
    main()