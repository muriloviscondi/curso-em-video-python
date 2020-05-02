print(
    '=-' * 10
    + '\nTriangle Analyzer\n' +
    '=-' * 10
)

a = float(input('Primeiro Segmento: '))
b = float(input('Segundo Segmento:  '))
c = float(input('Terceito Segmento: '))

if a < b + c and b < a + c and c < a + b:
    print(
        'Os seguimentos acima PODEM formar um triângulo'
    )
else:
    print(
        'Os seguimentos acima NÃO PODEM formar um triângulo'
    )