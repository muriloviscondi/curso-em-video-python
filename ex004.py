something = input('Digite algo: ')

print('O tipo primitivo desse valor é: {}'.format(type(something)))
print('Só tem espaços? {}'.format(something.isspace()))
print('É um numero? {}'.format(something.isnumeric()))
print('É alfabético? {}'.format(something.isalpha()))
print('É alfanumérico? {}'.format(something.isalnum()))
print('Está em maiúscula? {}'.format(something.isupper()))
print('Está em minúscula? {}'.format(something.islower()))
print('Está capitalizada? {}'.format(something.istitle()))

