preco = float(input('qual é o preco do produto?:R$'))

desconto = (preco*5/100)

print('Seu produto com desconto é R${:.2f}'.format(preco - desconto))
