sum = 0
count = 0

for i in range(1, 7, 1):
    num = int(input('Digite o {}o valor: '.format(i)))

    if num % 2 == 0:
        sum += num
        count += 1

print(
    'Você informou {} numeros pares.'
    '\nA soma de todos os numeros pares é {}.'
    .format(
        count,
        sum
    )
)