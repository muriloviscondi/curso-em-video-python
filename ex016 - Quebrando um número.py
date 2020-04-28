from math import trunc

num = float(input('Digite um valor: '))

print(
    'O valor digitado foi: {}'
    '\nSua porção inteira é: {:.0f}'
    '\nSua porção inteira é: {}'
    '\nSua porção inteira é: {}'
    .format(
        num,
        num,
        int(num),
        trunc(num)
    )
)