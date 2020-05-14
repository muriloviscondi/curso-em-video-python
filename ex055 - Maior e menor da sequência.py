less_weight = 0
more_weight = 0

for i in range(1, 6):
    weight = float(input(
        'Peso da {}ª pessoa: '
        .format(i))
    )

    if i == 1:
        less_weight = weight
        more_weight = weight
    elif weight < less_weight:
        less_weight = weight
    elif weight > more_weight:
        more_weight = weight

print(
    'O maior peso lido foi de {}kg'
    '\nO menor peso lido foi de {}kg'
    .format(
        more_weight,
        less_weight
    )
)