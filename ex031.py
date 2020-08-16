print('CALCULANDO PREÇO DE VIAGEM:\n'
      '')

dis = int(input('Digite sua distância em Km: '))
if dis <= 200:
    print('Foi cobrado ( R${:.2f} ) de sua viagem.'.format(dis * 0.50))
else:
    print('Foi cobrado ( R${:.2f} ) de sua viagem.'.format(dis * 0.45))
