n = str(input('Digite seu nome completo: ')).title().split()
nome = '<>'.join(n)
print('Muito prazer em te conhecer, {}!\n'
      'Seu primeiro nome é ( {} )\n'
      'E seu ultimo nome é ( {} )\n'
      '{}'
      .format(n [0], n [0], n [len(n) - 1], nome))

'''n = str(input('Digite')).split()
nome = '@'.join(n)
print(nome)'''