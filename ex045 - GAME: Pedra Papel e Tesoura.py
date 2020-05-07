from time import sleep
from random import randint

print(
    'Suas Opções:'
    '\n[ 0 ] Pedra'
    '\n[ 1 ] Papel'
    '\n[ 2 ] Tesoura'
)

player = int(input('Qual a sua jogada? '))

while player < 0 or player > 2:
    print('Jogada INVÁLIDA! As opções válidas são: 0, 1 ou 2.')
    player = int(input('Qual a sua jogada? '))

cpu = randint(0, 2)

print('JAN')
sleep(0.8)
print('KEN')
sleep(0.8)
print('PO!!!')

if player == 0:
    movePlayer = 'Pedra'
elif player == 1:
    movePlayer = 'Papel'
elif player == 2:
    movePlayer = 'Tesoura'

if cpu == 0:
    moveCpu = 'Pedra'
elif cpu == 1:
    moveCpu = 'Papel'
elif cpu == 2:
    moveCpu = 'Tesoura'

print(
    '=-' * 12 +
    '\nComputador jogou {}'
    '\nJogador jogou {}'
    .format(
        moveCpu,
        movePlayer
    )
)

print(
    '=-' * 12
)

if player == 0 and cpu == 2 or player == 1 and cpu == 0 or player == 2 and cpu == 1:
    print('JOGADOR VENCE!')
elif cpu == 0 and player == 2 or cpu == 1 and player == 0 or cpu == 2 and player == 1:
    print('COMPUTADOR VENCE!')
else:
    print('EMPATE!!!')




