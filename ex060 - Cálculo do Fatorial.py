num: int = int(
    input(
        'Digite um numero para calcular seu fatorial: '
    )
)

count = num
factorial: int = 1

while count > 0:
    if factorial == 1:
        print(
            'Calculando {}! = {} '
            .format(num, count),
            end=''
        )
    else:
        print(
            'x {} '
            .format(count),
            end=''
        )
    factorial *= count
    count -= 1

print(
    '= {}'
    .format(factorial)
)
