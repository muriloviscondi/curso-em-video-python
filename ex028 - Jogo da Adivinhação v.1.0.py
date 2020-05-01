from time import sleep
from random import randint

print(
    '-=' * 28
    + '\nVou pensar em um numero entre 0 e 5. Tente advinhar...\n'
    + '-=' * 28
)

num = int(input('Em que número pensei: '))

while (num > 5) or (num < 0):
    print(
        'ERRO! Valor digitado tem que estar entre 0 e 5!'
    )
    num = int(input('Em que número pensei: '))

pc = randint(0, 5)

print(
    '\nPROCESSANDO...'
)
sleep(2)

if num == pc:
    print(
        'PARABÉNS! Você conseguiu me vencer!GANHEI!'
    )
else:
    print(
        'GANHEI! Pensei no numero {} e nao {}!'
        .format(
            pc,
            num
        )
    )
