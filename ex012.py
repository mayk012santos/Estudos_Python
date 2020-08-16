preço = float(input('Qual o preço do produto? R$ '))
print('O produto que custava R$ {:.2f}, com desconto de 5% que vai ser de R$ {:.2f},\n'
      'O prouto vai sair para você por R$ {:.2f}.'
      .format(preço, (5 * preço) / 100, preço - ((5 * preço) / 100)))



