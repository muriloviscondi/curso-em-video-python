num = int(input('Digite um numero para ver sua tabuada: '))
count = 1

while count < 11:
    print(
        '{:2} x {:2} = {:2}'
        .format(num, count, num * count)
    )
    count += 1
