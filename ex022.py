nome = str(input('Digite o seu nome: '))
divide = nome.split()

print('Seu nome em letras MAIUSCULAS é: ( {} )!\n'
      'Seu nome com todas as letras MINUSCULAS é: ( {} )!\n'
      'Seu primeiro nome é ( {} ) e tem ( {} ) LETRAS.\n'
      'Seu nome no total seu nome tem ( {} ) letras. OBS: Desconsiderando os espaços.'
      .format(nome.upper(), nome.lower(), divide[0], len(divide [0]), len(nome) - nome.count(' ')))