num = int(input('Digite um numero inteiro: '))

print(
    'Analisando o numero {}'
    '\nUnidade: {}'
    '\nDezena: {}'
    '\nCentena: {}'
    '\nMilhar: {}'
    .format(
        num,
        num // 1 % 10,
        num // 10 % 10,
        num // 100 % 10,
        num // 1000 % 10,

    )
)