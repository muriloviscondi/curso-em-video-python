distance = float(input('Qual a distância de sua viagem? '))

if distance > 200:
    ticket = distance * 0.45
else:
    ticket = distance * 0.50

print(
    'Você está preste a começar uma viagem de {}km'
    '\nO preço de sua passagem será: R$ {:.2f}'
    .format(
        distance,
        ticket
    )
)