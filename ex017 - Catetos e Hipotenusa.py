from math import hypot

catetoOposto = float(input('Comprimento do cateto oposto: '))
catetoAdjascente = float(input('Comprimento do cateto adjscente: '))

print(
    'A hipotenusa vai medir: {:.2f}'
    .format(hypot(catetoOposto, catetoAdjascente))
)