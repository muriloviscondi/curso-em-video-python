name = str(input('Digite seu nome completo: ')).strip()

nameList = name.split()

print(
    'Prazer em te conhecer!'
    '\nSeu primeiro nome é {}'
    '\nSeu último nome é {}'
    .format(
        nameList[0].capitalize(),
        nameList[-1].capitalize()
    )
)