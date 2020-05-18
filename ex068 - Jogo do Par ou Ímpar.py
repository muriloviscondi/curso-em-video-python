from random import randint
from time import sleep

print(
    '=-' * 15,
    '\nVAMOS JOGAR PAR OU ÍMPAR\n' +
    '=-' * 15,
)

player_score: int = 0
cpu_score: int = 0

while True:
    print(
        'Player {} x {} Computador'
        .format(
            player_score, cpu_score
        )
    )

    player: int = int(input('Digite um valor: '))
    move: str = str(input('Par ou Ímpar? [P/I] ')).upper().strip()
    cpu: int = randint(0, 10)

    while move not in 'PI':
        print('Jogada Inválida!!')
        move: str = str(input('Par ou Ímpar? [P/I] ')).upper().strip()

    sum_result = player + cpu

    if sum_result % 2 == 0:
        call_odds = 'PAR'
    else:
        call_odds = 'IMPAR'

    print(
        '=-' * 15,
        '\nVocê jogou {} e o computador {}. Total de {} DEU {}\n'
        .format(player, cpu, sum_result, call_odds) +
        '=-' * 15
    )

    if move == 'P' and call_odds == 'PAR':
        print('Você VENCEU!')
        player_score += 1
    elif move == 'I' and call_odds == 'IMPAR':
        print('Você VENCEU!')
        player_score += 1
    else:
        print('Você PERDEU!')
        cpu_score += 1

    sleep(1)
    print('=-' * 15)
