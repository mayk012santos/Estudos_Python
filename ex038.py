print('{}{:^85}{}'.format('\033[1;34;43m','DESCOBRINDO QUAL O NÚMERO MAIOR:', '\033[m'))
print()
num1 = int(input('Digite um número inteiro qualquer: '))
num2 = int(input('Digite outro número inteiro qualquer: '))
print()
if num1 > num2:
    print('O número {} é maior que o número {}.'.format(num1, num2))
elif num2 > num1:
    print('O número {} é maior que o número {}.'.format(num2, num1))
else:
    print('Não tem número maior ou menor. Os números {} e {} são iguais.'.format(num1, num2))