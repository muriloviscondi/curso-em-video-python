total_adulthood: int
total_men: int = 0
total_woman_minority:int = 0

while True:
    print(
        '-' * 30,
        '\n     CADASTRE  UMA  PESSOA\n' +
        '-' * 30
    )

    age: int = int(input('Idade: '))
    gender: str = str(input('Sexo: [M/F] ')).upper().strip()

    print(
        '-' * 30,
    )

    if age >= 18:
        total_adulthood += 1

    if gender == 'M':
        total_men += 1

    if age <= 20 and gender == 'F':
        total_woman_minority += 1

    option: str = str(input('Quer continuar? [S/N] ')).upper().strip()

    while option not in 'SN':
        option: str = str(input(
            'Opção Inválida!'
            '\nQuer continuar? [S/N] ')
        ).upper().strip()

    if option == 'N':
        break

print(
        '-' * 30,
    )
print(
    'Total de pessoas com mais de 18 anos: {}'
    '\nAo todo temos {} homens cadastros'
    '\nE temos {} mulheres com menos de 20 anos'
    .format(
        total_adulthood, total_men, total_woman_minority
    )
)
print(
        '-' * 30,
    )