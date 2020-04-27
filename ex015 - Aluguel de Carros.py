diasAlugados = float(input('Quantos dias alugados? '))
kmRodados = float(input('Quantos km rodados? '))

totalPagar = (diasAlugados * 60) + (kmRodados * 0.15)

print(
    'O total a pagar é R$ {:.2f}'
    .format(totalPagar)
)