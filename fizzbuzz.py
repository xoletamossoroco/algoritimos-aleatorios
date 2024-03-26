def fizzbuzz(inicio, fim):
    for num in range(inicio, fim + 1):
        if num % 3 == 0 and num % 5 == 0:
            print('FizzBuzz')
        elif num % 3 == 0:
            print('Fizz')
        elif num % 5 == 0:
            print('Buzz')
        else:
            print(num)

inicio = int(input('Digite o número inicial do intervalo: '))
fim = int(input('Digite o número final do intervalo: '))

fizzbuzz(inicio, fim)