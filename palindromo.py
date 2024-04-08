print("---------------------")
print("______PALINDROMO______")
print("---------------------")

import string

def limpar_texto(texto):
    translator = str.maketrans("", "", string.punctuation + string.whitespace)
    texto_limpo = texto.translate(translator)
    return texto_limpo.lower()

def is_palindromo(texto):
    texto_limpo = limpar_texto(texto)
    return texto_limpo == texto_limpo[::-1]

def main():
    print("Bem-vindo ao Verificador de Palíndromos!")
    entrada = input("Por favor, digite uma palavra, frase ou número: ")

    resultado = is_palindromo(entrada)

    if resultado:
        print(f"'{entrada}' é um palíndromo.")
    else:
        print(f"'{entrada}' não é um palíndromo.")

if __name__ == "__main__":
    main()