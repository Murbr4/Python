altura = float(input('qual é a altura da sua parede?'))
largura = float(input('qual é a largura dessa parede?'))

area = altura * altura

print('sua parede tem a dimensão de {} x {} e sua área é de {}m'.format(altura,largura,area))

tinta = area/2

print('para pintar sua parede, voce precisará de {}L de tinta'.format(tinta))


