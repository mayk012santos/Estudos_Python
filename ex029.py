vel = int(input('Digite a velocidade do carro: Km/h '))
if vel <= 80:
    print('Sua velocidade foi de {}km/h.'.format(vel))
else:
    print('Sua velocidade foi de {}km/h.\n'
          'Você foi multado por ecesso de velocidade.\n'
          'Você vai precisar pagar ( R$ {:.2f} ) de multa.\n'
          'O limite de velocidade é dê {}km/h'
          .format(vel, ((vel - 80) * 7), 80))
print('Dirija sempre com segurança. Cinto de segurança salva vidas!')