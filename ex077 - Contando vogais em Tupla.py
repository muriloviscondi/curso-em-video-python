words = (
    'APRENDER',
    'PROGRAMAR',
    'LINGUAGEM',
    'PYTHON',
    'CURSO',
    'GRATIS',
    'ESTUDAR',
    'PRATICAR',
    'TRABALHAR',
    'MERCADO',
    'PROGRAMAR',
    'FUTURO'
)

for word in words:
    print(f'Na palavra {word} temos', end=' ')

    for letter in word:
        if letter in 'AEIOU':
            print(f'{letter.lower()}', end=' ')

    print()
