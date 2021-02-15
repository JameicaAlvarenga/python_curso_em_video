'''
Desenvolva um programa que leia o comprimento de três retas e diga ao usuário
se elas podem ou não formar um triângulo.
'''

l1= float(input('Valor 1:'))
l2= float(input('Valor 2:'))
l3= float(input('Valor 3:'))

if (l1+l2)>l3 and (l2+l3)>l1 and (l1+l3)>l2:
    print('Esses valores podem formar um triangulo')
else:
    print('Esses valores não podem formar um triangulo')