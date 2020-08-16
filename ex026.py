print('Descobrindo quantas LETRAS escolhida aparece na frase: ')

frase = str(input('Digite uma frase: ')).upper().strip()
letra = str(input('Digite uma letra para pesquisa: ')).upper().strip()
print('Seu total de letras na frase {}\n'
      ' É de {} letras.\n'
      'Sua letra ( " {} " ) aparece ( {} ) vezes na frase {} escolhida.\n'
      'Sua primeira letra ( "{}" ), aparece na posição {} de sua frase.\n'
      'Sua ultima letra ( "{}" ), aparece na posição {} de sua frase.'
      .format(frase, len(frase) - frase.count(' '), letra, frase.count(letra), frase,
              letra, frase.find(letra) + 1, letra, frase.rfind(letra) + 1 - frase.count(' ')))
