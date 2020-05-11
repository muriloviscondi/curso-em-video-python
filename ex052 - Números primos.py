num = int(input('Digite um numero: '))
count = 0

for i in range(1, num + 1):

    if (num % i) == 0:
        print('\033[33m', end='')
        count += 1
    else:
        print('\33[31m', end='')

    print(i, end=' ')


print(
    '\n\033[mO número {} foi divisível {} vezes'
    .format(
        num,
        count
    )
)

if count == 2:
    print(
        'E por isso ele É PRIMO!'
    )
else:
    print(
        'E por isso ele NÃO É PRIMO!'
    )
