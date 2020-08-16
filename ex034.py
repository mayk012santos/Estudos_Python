print('Sabendo a quantidade de almento do sálario:'
      '\n')
salario = float(input('Digite o seu sálario: R$'))

if salario <= 1250.00:
    print('Seu sálario era de ( R$ {:.2f} e com o aumento de 15% vai ser de\n'
          '\033[4;31;40m(R$ {:.2f})'
          .format(salario, salario + (salario * 15 / 100)))
else:
    print('Seu sálario era de ( R$ {:.2f} e com o aumento de 10% vai ser de (R$ {:.2f})'
          .format(salario, salario + (salario * 10 / 100)))