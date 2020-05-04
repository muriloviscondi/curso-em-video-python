num = int(input('Digite um numero inteiro: '))
print(
    'Escolha uma das bases para conversão:'
    '\n[ 1 ] Converter para BINÁRIO'
    '\n[ 2 ] Converter para OCTAL'
    '\n[ 3 ] Converter para HEXADECIMAL'
)
option = int(input('Sua opção: '))

if option == 1:
    print(
        '{} converido para BINÁRIO é igual a {}'
        .format(
            num,
            bin(num)[2:]
        )
    )
elif option == 2:
    print(
        '{} converido para OCTAL é igual a {}'
        .format(
            num,
            oct(num)[2:]
        )
    )
elif option == 3:
    print(
        '{} converido para HEXADECIMAL é igual a {}'
        .format(
            num,
            hex(num)[2:]
        )
    )