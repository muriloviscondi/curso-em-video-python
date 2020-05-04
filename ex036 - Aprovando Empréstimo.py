houseValue = float(input('Valor da casa: '))
salary = float(input('Salário do comprador: R$ '))
years = int(input('Quantos anos de financiamento? '))


monthlyPayment = houseValue / (years * 12);

print(
    'Para paga uma casa de R$ {:.2f} '
    'em {:.0f} anos '
    'a prestação será de R$ {:.2f}.'
    .format(
        houseValue,
        years,
        monthlyPayment
    )
)

if (salary * 0.30) > monthlyPayment:
    print(
        'Empréstimo poderá ser CONCEDIDO!'
    )
else:
    print(
        'Empréstimo NEGADO!'
    )
