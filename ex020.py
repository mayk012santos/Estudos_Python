import random

n1 = input('Digite seu nome: ')
n2 = input('Digite seu nome: ')
n3 = input('Digite seu nome: ')
n4 = input('Digite seu nome: ')
ordem = [n1, n2, n3, n4]
random.shuffle(ordem)
print('Sua ordem de apresentação é: {}'.format(ordem))