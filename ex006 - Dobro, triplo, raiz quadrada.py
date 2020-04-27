from math import sqrt

num = float(input('Digite um numero: '))

doble = num * 2
triple = num * 3
root = sqrt(num)

print(
      'Analisando  numero {}'
      '\nSeu dobro: {}'
      '\nSeu triplo: {}'
      '\nSua raiz quadrada: {:.2f}'
      .format(num, doble, triple, root)
)

