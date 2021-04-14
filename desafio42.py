'''Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que
tipo de triângulo será formado:

– EQUILÁTERO: todos os lados iguais

– ISÓSCELES: dois lados iguais, um diferente

– ESCALENO: todos os lados diferentes

'''
l1= float(input('Valor 1:'))
l2= float(input('Valor 2:'))
l3= float(input('Valor 3:'))

if (l1+l2)>l3 and (l2+l3)>l1 and (l1+l3)>l2:
    if l1 == l2 == l3:
        print('Esses valores podem formar um triangulo: EQUILÁTERO')
    elif l1 != l2 != l3 != l1:
        print('Esses valores podem formar um triangulo:ESCALENO ')
    else:
        print('Esses valores podem formar um triangulo: ISÓSCELES')
else:
    print('Esses valores não podem formar um triangulo')