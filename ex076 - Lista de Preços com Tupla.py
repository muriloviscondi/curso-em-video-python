prices: float = (
    'Lápis', 1.75,
    'Borracha', 2,
    'Caderno', 15.9,
    'Estojo', 25,
    'Transferidor', 4.2,
    'Compasso', 9.99,
    'Mochila', 120.32,
    'Canetas', 22.3,
    'Livro', 34.9
)

print('-' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-' * 40)

for pos in range(0, len(prices)):
    if pos % 2 == 0:
        print(f'{prices[pos]:.<30}', end='')
    else:
        print(f'R$ {prices[pos]:>7.2f}')

print('-' * 40)