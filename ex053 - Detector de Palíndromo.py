frase = str(input('Digite um frase: ')).upper().strip().split()

newFrase = ''.join(frase)
inverse = ''

for i in range(len(newFrase) -1, -1, -1):
    inverse += newFrase[i]

print(
    'O inverso de {} é {}'
    .format(
        newFrase,
        inverse
    )
)

if newFrase == inverse:
    print(
        'Temos um palíndromo'
    )
else:
    print(
        'A frase digitada não um palíndromo'
    )


