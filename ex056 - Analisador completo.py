old_age: int = 0

count: int = 0
media_age: float = 0

count_female: int = 0

for p in range(1, 5):
    print(
        '----- {}ª Pessoa -----'
        .format(p)
    )

    name: str = str(input('Nome: ')).strip()
    age: int = int(input('Idade: '))
    gender: str = str(input('Sexo [M/F]: ')).upper().strip()

    if gender == 'M' and age > old_age:
        old_name = name
        old_age = age

    if gender == 'F' and age < 20:
        count_female += 1

    count += 1
    media_age += age

print(
    'A média de idade do grupo é de {:.1f}.'
    '\nO Homem mais velho tem {} anos e se chama {}.'
    '\nAo todo são {} mulheres com menos de 20 anos.'
    .format(
        media_age / count,
        old_age, old_name.capitalize(),
        count_female
    )
)
