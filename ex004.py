#Faça um programa que leia algo pelo teclado e mostre
#na tela o seu tipo primitivo e todas as informações
#possíveis sobre ele.

n = input('Digite algo:')
print('O tipo primitivo desse valor é: {}'.format(type(n)))
print('Só tem espaço? {}'.format(n.isspace()))
print('É numerico ? {}'.format(n.isnumeric()))
print('É alfabetico? {}' .format(n.isalpha()))
print('É alfanumerico? {}' .format(n.isalnum()))
print('Está em maiúsculas? {}'.format(n.isupper()))
print('Está em minúsculo? {}' .format(n.islower()))
print('Está capitalizado? {}' .format(n.istitle()))
