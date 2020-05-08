num = int(input('Digite um numero para ver sua tabuada: '))

for i in range(1, 11, 1):
    print(
        '{} x {:2} = {:2}'
        .format(
            num,
            i,
            num * i
        )
    )