name = str(input('Digite seu nome comleto: ')).strip()

print('Seu nome MAIÚSCULO é: {}' .format(name.upper()))
print('Seu nome MINÚSCULO é: {}' .format(name.lower()))
print('Seu nome tem ao todo: {} letras' .format(len(name) - name.count(' ')))

name = name.split()
firstName = name[0]

print('Seu primerio nome tem ao todo: {} letras' .format(len(firstName)))
