print('CONVERTENDO REAIS BRASILEIROS ( R$ ) EM DÓLARES ( US$ ):')

dinheiro = float(input('Quantos reais ( R$ ) você tem na carteira? R$ '))

print('Com R$0{} reais você consegue converter em US${:.2f} dólares.'
      .format(dinheiro, (dinheiro / 5.33)))