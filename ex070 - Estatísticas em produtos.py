total = more_thousand = cheaper = 0

print(
    '-' * 30,
    '\n{:^30}'.format('LOJA  SUPER  BARATÃO') + '\n' +
    '-' * 30
)

while True:
    product: str = str(input('Nome do produto: ')).capitalize().strip()
    price: float = float(input('Preço: R$ '))

    total += price

    if price > 1000:
        more_thousand += 1

    if cheaper == 0:
        cheaper_product = product
        cheaper = price

    if price < cheaper:
        cheaper_product = product
        cheaper = price

    option: str = str(input('Quer continuar? ')).upper().strip()

    while option not in 'SN':
        option: str = str(input(
            'Opção Inválida\n'
            'Quer continuar? '
        )).upper().strip()

    if option == 'N':
        break

    print(
        '-' * 30
    )

print(
    '{:-^40}'.format(' FIM DO PROGRAMA '))

print(
    'O total da compra foi R$ {:.2f}'
    '\nTemos {} produtos custando mais de R$ 1000.00'
    '\nO produto mais barato foi {} custando R$ {:.2f}'
    .format(
        total,
        more_thousand,
        cheaper_product, cheaper
    )
)
