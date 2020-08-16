z = 'VERIFICANDO STATUS DE IMC (Indice De Massa Corporal).'
print('{:^85}'.format(z))
print()

p = float(input('Digite seu peso: (Kg) '))
a = float(input('Digite sua altura: (m) '))
imc = p / (a ** 2)
print()
print('''Você quer se auto responder ou que o programa te responda?
[1] COMPUTADOR RESPONDA:
[2] ME RESPONDER:''')
escolha = int(input('DIGITE SUA ESCOLHA: '))
print()
if escolha == 1:

    if imc < 18.5:
        print('Com seu peso {} e sua altura de {}. Seu IMC é de ( {:.1f} ).\n'
              'Você esta no status de {}ABAIXO DO PESO{}.'.format(p, a, imc, '\033[1;31;40m', '\033[m'))

    elif imc >= 18.5 and imc <= 25:
        print('Com seu peso {} e sua altura de {}. Seu IMC é de ( {:.1f} ).\n'
              'Você esta no status de {}PESO IDEAL{}.'.format(p, a, imc, '\033[1;32;40m', '\033[m'))

    elif imc > 25 and imc <= 30:
        print('Com seu peso {} e su altura de {}. Seu IMC é de ( {:.1f} ).\n'
              'Você esta no status de {}SOBREPESO{}.'.format(p, a, imc, '\033[1;31;43m', '\033[m'))

    elif imc > 30 and imc <= 40:
        print('Com seu peso {} e sua altura de {}. Seu IMC é de ( {:.1f} ).\n'
              'Você esta no status de {}OBESIDADE{}.'.format(p, a, imc,'\033[1;31;40m', '\033[m'))

    elif imc > 40:
        print('Com seu peso {} e sua altura de {}. Seu IMC é de ( {:.1f} ).\n'
              'Você esta no status de {}OBESIDADE MÓRBIDA{}.'.format(p, a, imc,'\033[1;31;40m', '\033[m'))

elif escolha == 2: