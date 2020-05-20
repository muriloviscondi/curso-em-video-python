print(
    '=' * 30,
    '\n{:^30}\n'.format('BANCO CEV') +
    '=' * 30,
)

value: int = int(input('Qual valor você quer sacar? R$ '))
total: int = value
total_note: int = 0
value_note = 50

while True:
    if total >= value_note:
        total_note += 1
        total -= value_note
    else:
        if total_note > 0:
            print(
                f'Total de {total_note} cédulas de R$ {value_note}'
            )
        if value_note == 50:
            value_note = 20
        elif value_note == 20:
            value_note = 10
        elif value_note == 10:
            value_note = 5
        elif value_note == 5:
            value_note = 2
        elif value_note == 2:
            value_note = 1

        total_note = 0

        if total == 0:
            break

print(
    '=' * 30,
    '\nVolte sempre ao BANCO CEV! Tenha um bom dia!'
)
