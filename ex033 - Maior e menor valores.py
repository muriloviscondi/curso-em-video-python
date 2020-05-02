number = [
    int(input('Digite o primeiro valor: ')),
    int(input('Digite o segundo valor:  ')),
    int(input('Digite o terceiro valor: '))
]

bigger = number[0]
lower = number[0]

for i in number:
    if i > bigger:
        bigger = i

    if i < lower:
        lower = i

print(
    'O menor valor digitado foi: {}'
    '\nO maior valor digitado foi: {}'
    .format(
        lower,
        bigger
    )
)
