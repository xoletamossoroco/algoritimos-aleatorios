print("---------------------")
print("________MEDIA________")
print("---------------------")

def calcular_media(notas):
    total = sum(notas)
    return total / len(notas)

def verificar_aprovacao(media):
    return "Aprovado" if media >= 5 else "Reprovado"

def main():
    notas = []
    for i in range(1, 5):
        nota = float(input(f"Digite a nota do {i}º bimestre: "))
        notas.append(nota)

    media = calcular_media(notas)
    situacao = verificar_aprovacao(media)

    print("=== Resultado da Avaliação ===")
    print(f"Média final: {media:.2f}")
    print(f"Situação do aluno: {situacao}")

if __name__ == "__main__":
    main()