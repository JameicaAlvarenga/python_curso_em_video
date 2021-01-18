'''
Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
'''

from math import sin,cos,tan,radians
angulo = float(input('Informe o valor do angulo: '))
sen = sin(radians(angulo))
tan = tan(radians(angulo))
cos = cos(radians(angulo))

print ('Dado o angulo {} o valor do seno é: {:.2f}, do coseno é: {:.2f} e da tagente é: {:.2f}.'.format(angulo,sen,cos,tan))