'''Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.

'''

from math import trunc

num = float((input('Informe um numero: ')))
result = trunc(num)
print('O numero digitado foi: {:.2f},e a parte inteira de é: {}'.format(num, result))