from time import sleep
from datetime import date
atual = date.today().year # pegando ano atual
print(atual)
print('{}{:^85}{}'.format('\033[1;32;44m', 'LISTAMENTO MILITAR:', '\033[m'))
print()
ano = int(input('DIGITE O SEU ANO DE NASCIMENTO: '))
if ano > atual:
    sleep(1)
    print('{}ERRO! TENTE NOVAMENTE!!!{}'.format('\033[1;31;40m', '\033[m'))
else:

    print('''SUAS OPÇÕES: 
    [1] SE FOR MULHER
    [2] SE FOR HOMEM
    [3] SE JÁ SE ALISTOU''')
    sleep(1/5)
    resposta = int(input('DIGITE AQUI: '))
    if resposta == 1:
        sleep(1)
        print('MULHERES NÃO PRECISAM SE ALISTAR!')

    elif resposta == 2:
        if atual - ano > 18:
            sleep(1)
            print('{}SEU ALISTAMENTO FOI NO ANO DE {}! SE JÁ SE PASSARAM {} ANOS. ESTA MULTADO!{}'
                  .format('\033[4;31;40m', (ano + 18), atual - (ano + 18), '\033[m'))
        elif ano > atual:
            sleep(1)
            print('{}ERRO! TENTE NOVAMENTE: {}'.format('\033[4;31;40m', '\033[m'))

        elif atual - ano < 18:
            sleep(1)
            print('{}Seu alistamento será no ano de {}. AINDA FALTAM {} ANOS.{}'
                  .format('\033[1;32;40m', (ano + 18), (ano + 18) - atual,'\033[m'))

        elif atual - ano == 18:
            sleep(1)
            print('CORRA! QUEM NASCEU EM {} O ALISTAMENTO É ESSE ANOS DE {}!\n'
                  '{}NÃO SE ATRASE OU OCORRERA MULTA!{}'
                .format(ano, (ano + 18), '\033[1;31;40m', '\033[m'))
    elif resposta == 3:
        sleep(1)
        print('{}SEU ALISTAMENTO FOI NO ANO DE {}! SE PASSARAM {} ANOS.{}'
              .format('\033[4;31;40m', (ano + 18), atual - (ano + 18), '\033[m'))

    else:
        print('{} SUA ESCOLHA ( {} ) É INVALIDA! {}'.format('\033[1;31;40m', resposta, '\033[m'))
