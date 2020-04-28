from math import sin, cos, tan, radians

angulo = float(input('Digite o angulo que você deseja: '))

seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))

print(
    'O angulo de {:.1f}º tem:'
    '\nSENO:     {:.2f}'
    '\nCOSSENO:  {:.2f}'
    '\nTANGENTE: {:.2f}'
    .format(
        angulo,
        seno,
        cosseno,
        tangente
    )
)