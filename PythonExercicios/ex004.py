n = input('Digite algo:')

print('o tipo primitivo é {}'.format(type(n)))

print('Só tem espaço? ', n.isspace())

print('É um número? ', n.isnumeric())

print('É alfabético? ', n.isalpha())

print('É minúsculo? ', n.islower())

print('É Maiúsculo? ', n.isupper())

print('É alfanumérico? ', n.isalnum())

print('É capitalizada? ', n.istitle())