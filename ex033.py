print('Digite 3 valores:')

a = int(input('Digiite o 1° número: '))
b = int(input('Digite o 2° nímero: '))
c = int(input('Digite o 3° número: '))

#VERIFICANDO O MENOR:
menor = a
if b < a and b < c:
    nenor = b
if c < a and c < b:
    menor = c
# VERIFICANDO O MAIOR:

maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:you
print('O  MENOR valor digitado foi {}\n'
      'O MAIOR valor digitado foi {}'.format(menor, maior))