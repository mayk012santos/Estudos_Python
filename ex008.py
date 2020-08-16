medida = float(input('Digite sua medida em metro:'))

mm = medida * 1000
cm = medida * 100
dm = medida * 10
dam = medida / 10
hm = medida / 100
km = medida / 1000

print('Suas medidas são:\n'
      '{}mm\n'
      '{}cm\n'
      '{}dm\n'
      '{}m\n'
      '{}dam\n'
      '{}hm\n'
      '{}km'
      .format(mm, cm, dm, medida, dam, hm, km))