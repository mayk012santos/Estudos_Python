num = int(input('Digite um número: '))
print('Anlisando o seu número ( {} ), ele tem:\n'
      'Sua UNIDADE vale ( {} )\n'
      'Sua DEZENA vale ( {} )\n'
      'Sua CENTENA vale ( {} )\n'
      'Sua MILHAR vale ( {} )'
      .format(num, num // 1 % 10, num // 10 % 10, num // 100 % 10, num // 1000 % 10))