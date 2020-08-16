from time import sleep
from random import randint

a = 'JOGO DO JOKENPÔ'
armas = ('PEDRA', 'PAPEL', 'TESOURA')
computador = randint(0, 2)

print('''{}{:^85}{}
[0] PEDRA
[1] PAPEL
[2] TESOLRA'''.format('\033[3;34;43m', a, '\033[m'))
jogador = int(input('DIGITE SUA ESCOLHA: '))
sleep(1)
print('JÓ')
sleep(1)
print('KEN')
sleep(1)
print('PO')
sleep(1)
print('O COMPUTADOR JOGOU {}'.format(armas[computador]))
sleep(1)
print('O JOGADOR ESCOLHEU {}'.format(armas[jogador]))

if computador == 0:  # COMPUTADOR JOGOU PEDRA
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR GANHA!')
    elif jogador == 2:
        print('JOGADOR PERDE!')
    else:
        print('JOGADA INVALIDA!')
elif computador == 1:  # COMPUTADOR JOGOU PAPEL
    if jogador == 0:
        print('JOGADOR PERDE!')

    elif jogador == 1:
        print('EMPATE!')

    elif jogador == 2:
        print('JOGADOR VENCE!')

    else:
        print('JOGADA INVALIDA!')

elif computador == 2:  # COMPUTADOR JOGOU TESOURA
    if jogador == 0:
        print('JOGADOR VENCE!')

    elif jogador == 1:
        print('JOGADO0R PERDE!')

    elif jogador == 2:
        print('EMPATE!')

    else:
        print('JOGADA INVALIDA!')

