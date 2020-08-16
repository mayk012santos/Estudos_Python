import random
n1 = input('Digite seu nome: ')
n2 = input('Digite seu nome: ')
n3 = input('Digite seu nome: ')
n4 = input('Digite seu nome: ')
lista = [n1, n2, n3, n4]

escolhido = random.choice(lista)
print('O nome escolhido foi {}!'.format(escolhido))


