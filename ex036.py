a = 'FINANCIAMENTO DE CASA:'
print('{:=^80}'.format(a))

casa = float(input('Qual o valor da casa? R$ '))
salario = float(input('Qual o valor de seu salario? R$ '))
prestação = int(input('Em quantos anos deseja pagar sua casa? ')) * 12
pagar = (salario * prestação) - casa
print('Com a casa de ( R${:.2f} ), e o salario de ( R${:.2f} ), com as '
      '\nmensalidades de ( R${:.2f} ), em {} meses:'
      .format(casa, salario, casa / prestação, prestação))

if (salario - (salario * 30) / 100) * prestação < pagar:
    print('{}SEU FINANCIAMENTO FOI ACEITO!{}\n{}PARABÉNS!!!{}'
          .format('\033[4;32;40m', '\033[m','\033[4;32;40m', '\033[m'))

else:
    print('{}SEU FINANCIAMENTO FOI NEGADO!{}'.format('\033[1;31;40m', '\033[m'))