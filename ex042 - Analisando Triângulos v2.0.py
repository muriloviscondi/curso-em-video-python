a = float(input('Primeiro seguimento: '))
b = float(input('Segundo seguimento:  '))
c = float(input('Terceiro seguimento: '))

if a < b + c and b < a + c and c < a + b:
    if a == b == c:
        print('Os seguimentos acima PODEM FORMAR um Triângulo EQUILÁTERO.')
    elif a == b != c or b == c != a or c == a != b:
        print('Os seguimentos acima PODEM FORMAR um Triângulo ISÓSCELES.')
    elif a != b != c:
        print('Os seguimentos acima PODEM FORMAR um Triângulo ESCALENO.')
else:
    print("Os seguimentos acima NÃO PODEM formar um triângulo")
