dias = int(input('Quantos dias você ficou com o carro: '))
km = float(input('quantos km rodado: '))

total = (dias * 60) + (km * 0.15)

print('O preço total a pagar é {:.2f}'.format(total))