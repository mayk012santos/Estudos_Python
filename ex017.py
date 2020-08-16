'''from math import hypot

co = float(input('Digite seu cateto oposto: '))
ca = float(input('Digite  seu cateto adjacente: '))
h = hypot(co, ca)
print('Sua hipotenusa mede {:.2f}\n'
      'Seu cateto oposto medi {:.2f}\n'
      'Seu cateto adjacente medi {:.2f}'
      .format(h, co, ca))'''

co = float(input('Digite seu cateto oposto: '))
ca = float(input('Digite seu cateto adjacente: '))
hi = (co ** 2 + ca ** 2) ** (1/2)
print('Seu co medi {}, seu ca medi {} e sua hi medi {:.2f}'.format(co, ca, hi))