price = float(input('Preço das compras: R$ '))

print(
    'FORMAS DE PAGAMENTO'
    '\n[ 1 ] à vista dinheiro/cheque'
    '\n[ 2 ] à vista cartão'
    '\n[ 3 ] 2x no cartão'
    '\n[ 4 ] 3x ou mais no cartão'
)

option = int(input('Qual é a opção? '))

while option < 1 or option > 4:
    print("Opção INVÁLIDA! Opções entre 1 a 3.")
    option = int(input('Qual é a opção? '))

if option == 1:
    finalPrice = price - (price * 0.10)
elif option == 2:
    finalPrice = price - (price * 0.05)
elif option == 3:
    print(
        'Sua compra será parcelada em 2x de R$ {:.2f} SEM JUROS'
        .format(price / 2)
    )
    finalPrice = price
elif option == 4:
    parcel = int(input('Quantas parcelas? '))
    finalPrice = price + (price * 0.20)
    print(
        'Sua compra será parcelada em {}x de R$ {:.2f} COM JUROS'
        .format(
            parcel,
            finalPrice / parcel
        )
    )

print(
    'Sua compra de R$ {:.2f} vai custar R$ {:.2f} no final'
    .format(
        price,
        finalPrice
    )
)
