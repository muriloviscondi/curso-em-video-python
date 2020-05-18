sum_total = count = small_number = large_number = 0

while True:
    num = int(input('Digite um número: '))

    if count == 0:
        small_number = num
        large_number = num
    else:
        if num > large_number:
            large_number = num
        if num < small_number:
            small_number = num

    sum_total += num
    count += 1

    option = str(input('Quer continuar?[S/N] ')).upper().strip()

    while option not in 'SN':
        print('Opção Inválida!')
        option = str(input('Quer continuar?[S/N] ')).upper().strip()

    if option == 'N':
        break

print(
    'Você digitou {} números e a média foi {:.2f}'
    '\nO maior valor foi {} e o menor foi {}'
    .format(
        count, sum_total / count,
        large_number, small_number
    )
)
