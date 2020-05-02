speed = float(input('Qual a velocidade atual do carro? '))

if speed > 80:
    ticket = (speed - 80) * 7
    print(
        'MULTADO! Você excedeu o limite de velocidade que é de 80km/h'
        '\nVocê deve pagar uma multa de: R$ {:.2f}'
        .format(
            ticket
        )
    )

print(
    'Tenha um bom dia! Dirija com segurança!'
)