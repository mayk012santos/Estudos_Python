from time import sleep
a = 'APROVAÇÃO DE ALUNO:'
print('{:^85}'.format('APROVAÇÃO DE ALUNO:'))

n1 = float(input('DIGITE SUA PRIMEIRA NOTA: '))
n2 = float(input('DIGITE SUA SEGUNDA NOTA: '))
m = (n1 + n2) / 2

if m >= 7:
    sleep(1)
    print('COM A MÉDIA ( {:.1f} ), {}VOCÊ ESTA APROVADO! CONTINUE ASSIM. PARABÉNS!!!{}'
          .format(m, '\033[4;32;40m', '\033[m'))
elif m >= 5.0 and m < 7.0:
    sleep(1)
    print('COM A MÉDIA ( {:.1f} ) {}VOCÊ ESTA EM RECUPERAÇÃO!{}'
          .format(m, '\033[4;31;43m', '\033[m'))
else:
    sleep(1)
    print('COM A MÉDIA ( {:.1f} ) {}VOCÊ ESTA REPROVADO!{}'
          .format(m, '\033[1;31;40m', '\033[m'))
