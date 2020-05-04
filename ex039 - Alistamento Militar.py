from datetime import date

yearBirth = int(input('Ano de nascimento: '))
age = date.today().year - yearBirth

print(
    'Quem nasceu em {} tem {} anos em {}.'
    .format(
        yearBirth,
        age,
        date.today().year
    )
)

if age > 18:
    print(
        'Vocẽ já prestou ou deveria ter prestado serviço militar em {}'
        .format(
            date.today().year - (age - 18)
        )
    )
elif age == 18:
    print(
        'Seu alistamento será este ano!'
    )

else:
    if (18 - age) == 1:
        print(
            'Ainda falta {} ano para o alistamento.'
            .format(
                18 - age,
            )
        )
    else:
        print(
            'Ainda falta {} anos para o alistamento.'
            .format(
                18 - age,
            )
        )

    print(
        'Seu alistamento será em {}.'
        .format(
            date.today().year + (18 - age)
        )
    )
