'''
 Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
'''

num = (input('Digite um numero de 0 a 9999: '))
aux = len(num)
i=(0)

if len(num) > 4:
    print('O numero digitado precisa estar entre 0 e 9999')
else:
   while i < aux+1:
        print(num[i])
        i += 1

