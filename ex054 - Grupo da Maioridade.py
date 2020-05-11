from datetime import date

today = date.today().year
older = 0
younger = 0

for i in range(1, 8):
    age = int(input('Digite o ano de nascimento da {}a passoa: ' .format(i)))

    if (today - age) <= 18:
        younger += 1
    else:
        older += 1

print(
    '\nAo todo tivemos {} pessoas maiores de idade'
    '\nE também tivemos {} menores de idade'
    .format(
        older,
        younger
    )
)