num = int(input('Digite um número qualquer: '))
print('Seu número digitado foi {}\n'
      'O dobro do número {} é {}\n'
      'O triplo é {} \n'
      'E sua raiz quadrada é {:.2f}'
      .format(num, num, num + num, num * 3, num ** (1/2)))