import math

angulo = float(input('Digite o ângulo desejado: '))
Seno = math.sin(math.radians(angulo))
Cosseno = math.cos(math.radians(angulo))
Tangente = math.tan(math.radians(angulo))

print('Seu ângulo desejado foi {}\n'
      'Seu SENO medi {:.2f}\n'
      'Seu COSSENO medi {:.2f}\n'
      'Sua TANGENTE medi {:.2f}'.format(angulo, Seno, Cosseno, Tangente))