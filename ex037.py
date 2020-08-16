print('<==>' * 40)
print()
z = ' CONVERSÃO DE NÚMERO: '
print('{:=^85}'.format(z))
print()
print('<==>' * 40)

num = int(input('Digite um número: '))

print('''Você deseja converter seu numero {} em o que?
[1] BINÁRIO
[2] OCTAL
[3] HEXADECIMAL
'''.format(num))
escolha = int(input('QUAL A SUA ESCOLHA? '))

if escolha == 1:
    print('Sua escolha foi conversão em BINÁRIO é igual a: {}'.format(bin(num)[2:]))
elif escolha == 2:
    print('Sua escolha foi conversão para OCTAL é igual a: {}'.format(oct(num)[2:]))
elif escolha == 3:
    print('Sua escolha foi conversão em BINÁRIO é igual a: {}'.format(hex(num)[2:]))
else:
    print('{} SUA ESCOLHA ( {} ) É INVALIDA! {}'.format('\033[1;31;40m', escolha, '\033[m'))