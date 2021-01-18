'''
Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo.
Calcule e mostre o comprimento da hipotenusa.

'''

import math

cateto_oposto = float(input('Informe o primeiro cateto oposto:'))
cateto_adjacente =  float(input('Informe o cateto adjacente: '))

result = math.hypot(cateto_oposto,cateto_adjacente)
print('Dado os  valores {} , {} o calculo da hipotenusa é {}:'.format(cateto_oposto,cateto_adjacente,result))