weight = float(input('Qual o seu peso?   '))
height = float(input('Qual a sua altura? '))

bmc = weight / pow(height, 2)

print(
    'Seu IMC é: {:.1f}'
    .format(
        bmc
    )
)

if bmc < 18.5:
    print('Você está ABAIXO DO PESO.')
elif bmc < 25:
    print('Você está no PESO IDEAL.')
elif bmc < 30:
    print('Você está com SOBREPESO.')
elif bmc < 40:
    print('Você está com OBESIDADE.')
else:
    print('Você está com OBESIDADE MORBIDA.')