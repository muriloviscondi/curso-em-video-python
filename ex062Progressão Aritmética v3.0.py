from time import sleep

print(
    'Gerador de PA \n',
    '-=' * 10
)

term: int = int(input('Primeiro termo: '))
ratio: int = int(input('Razão da PA: '))

pa: int = term
ratio_original: int = ratio
ratio_count = 10
sum_ratio: int = 10
count: int = 0

while ratio != 0:
    while count < ratio_count:
        print(
            '{} -> '
            .format(pa),
            end=''
        )

        pa += ratio_original
        count += 1

    print('PAUSA')
    ratio: int = int(
        input(
            'Quantos termos você quer mostrar a mais? '
        )
    )
    count: int = 0
    ratio_count = ratio
    sum_ratio += ratio

print(
    'Finalizando...'
)

sleep(2)

print(
    '\nProgressão finalizada com {} termos mostrados.'
    .format(sum_ratio)
)
