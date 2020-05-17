num_break = 0
count = 0
sum_total = 0

while num_break != 999:
    num = int(input('Digite um número [999 para parar]: '))

    if num == 999:
        num_break = 999
    else:
        sum_total += num
        count += 1

print(
    'Você digitou {} números e a soma entre eles foi {}.'
    .format(
        count, sum_total
    )
)
