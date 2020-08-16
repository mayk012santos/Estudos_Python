from datetime import date
ano = int(input('Digite ( 0 ) para saber o ano atual '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('Seu ano {} É BISSEXTO!'.format(ano))
else:
    print('O ano {} NÃO é BISEXTO!'.format(ano))

