nome = str(input('Como gosta de ser chamadx? '))

n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
n3 = float(input('Digite sua terceira nota: '))
n4 = float(input('Digite sua quarta nota: '))
medano = (n1 + n2 + n3 + n4) // 4
print('Sua média anual foi ( {:.1f} )'.format(medano))

if medano >= 6:
    print('Com a média anual de ( {} ), você esta aprovadx, {}! Paraéns!!!'
          .format(medano, nome))

elif medano >= 5 and medano <= 6.9:
    print('Com a media anual de ( {} ), você esta em recuperação, {}! Se exforce para não ser reprovado.'
          .format(medano, nome))

else:
    print('Com a média anual de ( {} ), você esta reprovadx, {}! Estude mais próximo ano.'
          .format(medano, nome))
