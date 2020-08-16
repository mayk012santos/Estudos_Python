z = 'DANDO DESCONTO OU JUROS NA COMPRA:'
print('{:^85}'.format(z))

preço = float(input('Qual o valor do produto? R$ '))

print('''Qual sua forma de pagamento?

[1] DINHEIRO/CHEQUE:

[2] Á VISTA NO CARTÃO:

[3] PARCELADO:
''')

resposta = int(input('Digite os seguintes números das compras: '))

if resposta == 1:
    d = preço - ((preço * 10) / 100)
    print(' O produto que custava ( R$ {:.2f} ), com desconto, vai lhe custar ( R$ {:.2f} ) '
          .format(preço, d))

elif resposta == 2:
    d = preço - ((preço * 5) / 100)
    print(' O produto que custava ( R$ {:.2f} ), com desconto, vai lhe custar ( R$ {:.2f} ) '
          .format(preço, d))
elif resposta == 3:
    p = int(input('Em quantas vezes você pretende parcelar? '))
    if p <= 2:
        print('Você não teve acrecemo nem desconto do produto de ( R$ {:.2f} ).\n'
              'Serão {}X de ( R$ {:.2f} ) por mês )'.format(preço, p, preço / p))
    elif p >= 3:
        d = preço + ((preço * 20) / 100)
        print('O produto que custava ( R$ {:.2f} ), no acrecemo vai lhe custar ( R$ {:.2f} ).'
              .format(preço, d))
        print('Serão {}X de ( R$ {:.2f} ) por mês'.format(p, d / p))

elif resposta > 3:
    print('\033[1;30;41m''-=' * 8, 'ERRO!', '-=' * 8, '-=' * 0, 'ERRO!', '-=' * 8,'-=' * 0,
          'ERRO!', '-=' * 8, '\033[m')

