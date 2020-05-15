gender: str = str(input('Informe seu sexo: [M/F] ')).upper().strip()

while gender not in 'MF':
    gender: str = str(
        input(
            'Dados Inválidos. Digite M ou F.'
            '\nInforme seu sexo: '
        )).upper()

print(
    'Sexo {} registrado com sucesso'
    .format(gender)
)
