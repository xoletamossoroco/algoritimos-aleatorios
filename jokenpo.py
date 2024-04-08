print("---------------------")
print("_PEDRA PAPEL TESOURA_")
print("---------------------")

from colorama import Fore, Style

def verificar_vencedor(jogador1, jogador2):
    if jogador1 == jogador2:
        return Fore.YELLOW + "Empate" + Style.RESET_ALL
    elif (jogador1 == 'Pedra' and jogador2 == 'Tesoura') or \
         (jogador1 == 'Tesoura' and jogador2 == 'Papel') or \
         (jogador1 == 'Papel' and jogador2 == 'Pedra') or \
         (jogador1 == 'Pedra' and jogador2 == 'Lagarto') or \
         (jogador1 == 'Lagarto' and jogador2 == 'Spock') or \
         (jogador1 == 'Spock' and jogador2 == 'Tesoura') or \
         (jogador1 == 'Tesoura' and jogador2 == 'Lagarto') or \
         (jogador1 == 'Lagarto' and jogador2 == 'Papel') or \
         (jogador1 == 'Papel' and jogador2 == 'Spock') or \
         (jogador1 == 'Spock' and jogador2 == 'Pedra'):
        return Fore.GREEN + "Jogador 1 vence" + Style.RESET_ALL
    else:
        return Fore.BLUE + "Jogador 2 vence" + Style.RESET_ALL

def main():
    print(Fore.CYAN + "Bem-vindo ao Jogo Jokenpo!" + Style.RESET_ALL)

    while True:
        jogador1 = input("Jogador 1, escolha Pedra, Papel, Tesoura, Lagarto ou Spock: ").capitalize()
        jogador2 = input("Jogador 2, escolha Pedra, Papel, Tesoura, Lagarto ou Spock: ").capitalize()

        if jogador1 not in ['Pedra', 'Papel', 'Tesoura', 'Lagarto', 'Spock'] or jogador2 not in ['Pedra', 'Papel', 'Tesoura', 'Lagarto', 'Spock']:
            print(Fore.RED + "Opção inválida. Por favor, escolha apenas entre Pedra, Papel, Tesoura, Lagarto, Spock." + Style.RESET_ALL)
            continue

        resultado = verificar_vencedor(jogador1, jogador2)
        print("Resultado:", resultado)

        jogar_novamente = input("Deseja jogar novamente? (sim/não): ").lower()
        if jogar_novamente != 'sim':
            print(Fore.CYAN + "Obrigado por jogar. Até mais!" + Style.RESET_ALL)
            break

main()