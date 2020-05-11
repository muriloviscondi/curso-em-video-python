term = int(input('Primeiro termo: '))
reason = int(input('Razão: '))

for i in range(1, 11):
    print(
        '{} -> '
        .format(
            term
        ),
        end=''
    )
    term += reason

print('Acabou')