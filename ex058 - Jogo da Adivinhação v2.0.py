from random import randint

print(
    'Sou seu computador...'
    '\nAcabei de pensar em um número inteiro entre 0 e 10'
)

player: int = int(input('Qual o seu palpite? '))
cpu: int = randint(0, 10)
count = 0

while player != cpu:

    if player < cpu:
        print(
            'Mais... Tente mais uma vez'
        )
    elif player > cpu:
        print(
            'Menos... Tente mais uma vez'
        )

    player: int = int(input('Qual o seu palpite? '))
    count += 1

print(
    'Acertou em {} tentativas. Parabéns!'
    .format(
        count + 1
    )
)
