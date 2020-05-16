print(
    'Gerador de PA \n',
    '-=' * 10
)

term: int = int(input('Primeiro termo: '))
ratio: int = int(input('Razão da PA: '))

pa: int = term
count: int = 0

while count < 10:
    print(
        '{} -> '
        .format(pa),
        end=''
    )

    pa += ratio
    count += 1

print('FIM')