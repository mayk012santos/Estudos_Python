print('AUMENTO DE SALÁRIO:')

sal = float(input('Digite seu salário atual: R$ '))
print('Seu salário anterior era de ( R${:.2f} ).\n'
      'Com o aumento de 15% seu salário atual é de ( R${:.2f} ).'
      .format( sal, ((sal * 15) / 100) + sal))
