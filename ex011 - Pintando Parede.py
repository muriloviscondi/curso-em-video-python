largura = float(input('Largura da parede: '))
altura = float(input('Altura da parede: '))

area = largura * altura
litroTinta = area / 2

print(
    'Sua parede tem a dimensão de  {} x {} e sua área é de {:.2f}m²'
    '\nPara pintar essa parede você precisára de {:.2f} litros de tinta'
    .format(
        largura,
        altura,
        area,
        litroTinta
    )
)