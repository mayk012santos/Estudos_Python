from datetime import date
from time import sleep
atual = date.today().year
a = 'RECONHECENDO SUA CATEGORIA COMO NADADOR(A):'
print('{:^85}'.format('RECONHECENDO SUA CATEGORIA COMO NADADOR(A):'))

ano = int(input('DIGITE SEU ANO DE NASCIMENTO: '))
c = atual - ano
if c <= 9:
    sleep(1)
    print('COM {} ANOS, {}VOCÊ É UM ATLETA MIRIM.{}'
          .format(c, '\033[1;32;40m', '\033[m'))
elif c > 9 and c <= 14:
    sleep(1)
    print('COM {} ANOS, {}VOCÊ É UM ATLETA INFANTIL.{}'
          .format(c, '\033[1;32;40m', '\033[m'))
elif c > 14 and c <= 19:
    sleep(1)
    print('COM {} ANOS, {}VOCÊ É UM ATLETA JUNIOR.{}'
          .format(c, '\033[1;32;40m', '\033[m'))
elif c > 19 and c <= 25:
    sleep(1)
    print('COM {} ANOS, {}VOCÊ É UM ATLETA SÊNIOR.{}'
          .format(c, '\033[1;32;40m', '\033[m'))
elif c > 25:
    sleep(1)
    print('COM {} ANOS, {}VOCÊ É UM ATLETA MASTER.{}'
          .format(c, '\033[1;32;40m', '\033[m'))