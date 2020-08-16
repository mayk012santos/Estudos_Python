print('VERIFICAÇÃO DE ALUGUEL DO CARRO:')

dias = int(input('Quantos dias o carro foi alugado? '))
km = float(input('Quantos km o carro rodou? '))

print('Você alugou o carro por {} dias.\n'
      'Você precisara pagar R${:.2f} de aluguel por dias e\n'
      'Precisará pagar R${:.2f} por km rodado.\n'
      'Seu total apagar vai ser de R${:.2f}.\n'
      'Volte sempre em nossa loja.'
      .format(dias, dias * 60, 0.15 * km, ((dias * 60) + (0.15 * km ))))
