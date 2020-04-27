real = float(input('Quanto dinheiro você tem na carteira? '))
dolar = float(input('Qual a cotação do dolar? '))

print(
    'Com R$ {:.2f} você pode comprar US$ {:.2f}'
    .format(real, real / dolar)
)