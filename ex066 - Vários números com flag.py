sum_values = count = 0

while True:
    num = int(input('Digite um valor (999 para parar): '))

    if num == 999:
        break

    sum_values += num
    count += 1

print(
    'A soma dos {} valores foi {}!'
    .format(count, sum_values)
)