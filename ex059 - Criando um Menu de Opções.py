from time import sleep

num1: int = int(input('Primeiro valor: '))
num2: int = int(input('Segundo valor: '))
option = 0

while option != 5:
    print(
        '\t[ 1 ] somar'
        '\n\t[ 2 ] multiplicar'
        '\n\t[ 3 ] maior'
        '\n\t[ 4 ] novos números'
        '\n\t[ 5 ] sair do programa'
    )
    option: int = int(input('>>>>> Qual a sua opção? '))

    if option == 1:
        print(
            'A soma entre {} e {} é {}'
            .format(
                num1, num2, num1 + num2
            )
        )
    elif option == 2:
        print(
            'A resultado de {} x {} é {}'
            .format(
                num1, num2, num1 * num2
            )
        )
    elif option == 3:
        if num1 > num2:
            bigger = num1
        else:
            bigger = num2

        print(
            'Entre {} e {} o maior valor é {}'
            .format(
                num1, num2, bigger
            )
        )
    elif option == 4:
        print('Informe os números novamente')
        num1: int = int(input('Primeiro valor: '))
        num2: int = int(input('Segundo valor: '))
    elif option == 5:
        print('Finalizando...')

    else:
        print(
            'Opção inválida. Tente novamente'
        )

    print(
        '=-=' * 10
    )

    sleep(2)

print(
    'Fim do Programa! Volte sempre!'
)
