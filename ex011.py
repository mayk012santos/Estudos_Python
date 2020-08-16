print('VAMOS SABER QUANTAS LATAS DE TINTA VOCÊ VAI PRECISAR PARA PINTAR A PAREDE: ')


h = float(input('Qual a sua ALTURA da parede em metros? '))
l = float(input('Qual a LARGURA da parede em metros? '))
a = h * l

print('Sua parede tem a dimenção de {}X{} e sua área é de {}m²'.format(h,l,a))
print('Para pintar toda parede você vai precisar de {}L de tinta.\n'
      'Considerando que cada ( 1L ) de tinta pinta 2m²'.format(a / 2))