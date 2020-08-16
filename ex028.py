from random import randint
from time import sleep
computador = randint(0, 5)#Fazendo_o_computador pensar
print('-=-' * 50)

pessoa = int(input('Digite um número: '))
print('\033[30;43m''AGUARDE...''\033[m')

print('-=-' * 50)
sleep(5)

if pessoa > 5:
      print('{}ERRO:\n'
            'NÃO EXISTE A ESCOLHA {}{}.\n'
            '{}TENTE NOVAMENTE{}'.format('\033[0;30;41m',
                                         pessoa, '\033[m',
                        '\033[4;30;42m', '\033[m'))
elif pessoa == computador:
      print('{}VOCÊ VENCE!{}\n'
            'Você escolheu {}( {} ){} e o computador {}( {} ){}'
            .format('\033[0;32;41m','\033[m',
            '\033[0;40;32m', pessoa, '\033[m',
                    '\033[4;30;41m', computador, '\033[m'))
elif computador != pessoa:
      print('{}COMPUTADOR VENCE!{}\n'
            'Você escolheu {}( {} ){}, e COMPUTADOR {}( {} ){}'
            .format('\033[0;30;41m', '\033[m',
                    '\033[0;32;41m', pessoa, '\033[m',
            '\033[4;30;41m', computador, '\033[m'))


else:
      print(computador)

print('\033[7;47m''-=-' * 50)

'''nome = str(input('Digite seu nome ou frase: ')).upper().strip()
nomee = nome.split()
n = nome.find('MAYK') + 1
o = nome.find('K') + 1
print('A palavra ( "{}" ) vai da posição {}° até a  posição {}° '
.format(nomee[0], n, o))
print('Existe a palavra ( "{}" ) na frase? ( {} )'
      .format(nomee [0],'MAYK' in nome))'''


