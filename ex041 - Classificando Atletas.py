from datetime import date

yearBirth = int(input('Ano de Nascimento: '))

age = date.today().year - yearBirth

print(
    'O atleta tem {} anos.'
    .format(
        age
    )
)

if age <= 9:
    classification = 'MIRIM'
elif age <= 14:
    classification = 'INFANTIL'
elif age <= 19:
    classification = 'JUNIOR'
elif age <= 25:
    classification = "SENIOR"
else:
    classification = "MASTER"

print(
    'Classificação: {}'
    .format(
        classification
    )
)