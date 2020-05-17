print(
    '-' * 30,
    '\nSequência de Fibonacci\n' +
    '-' * 30
)

term = int(input('Quantos termos você quer mostrar? '))

inicial_number = 0
next_number = 1
sum = 0
count = 0

while count < term:
    print(
        '{} -> '
        .format(inicial_number),
        end=''
    )

    sum = inicial_number + next_number
    inicial_number = next_number
    next_number = sum

    count += 1

print('FIM')

print(
    '~' * 30
)

print(
    '~' * 30
)
