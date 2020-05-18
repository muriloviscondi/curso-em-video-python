while True:
    num: int = int(input('Quer ver a tabudada de qual valor? '))
    print('-' * 30)

    if num < 0:
        break

    for i in range(1, 11):
        print(
            '{} x {:2} = {:3}'
            .format(
                num, i, num * i
            )
        )
    print('-' * 30)

print('PROGRAMA TABUADA ENCERRADO. Volte Sempre!!!')
