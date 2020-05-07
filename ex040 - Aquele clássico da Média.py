n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota:  '))

mean = (n1 + n2) / 2

print(
    'Tirando {:.1f} e {:.1f}, '
    'A média do aluno  é {:.1f}'
    .format(
        n1,
        n2,
        mean
    )
)

if mean < 5:
    print(
        'Aluno REPROVADO'
    )
elif mean < 7:
    print(
        'Aluno em RECUPERAÇÃO'
    )
else:
    print(
        'Aluno APROVADO'
    )