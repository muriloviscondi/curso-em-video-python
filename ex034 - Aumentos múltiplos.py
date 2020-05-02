salary = float(input('Qual é o salário do funcionário? R$ '))

if salary > 1250:
    newSalary = salary + (salary * 0.10)
else:
    newSalary = salary + (salary * 0.15)

print(
    'Quem ganhava:........ R$ {:.2f},'
    '\nPassa a granhar:.... R$ {:.2f}'
    .format(
        salary,
        newSalary
    )
)
