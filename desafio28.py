'''
Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e
peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
O programa deverá escrever na tela se o usuário venceu ou perdeu.


'''

import random

seq = [0, 1, 2, 3, 4, 5]
n1=random.choice(seq)
n= int(input('Digite um valor de 0 a 5: '))
if n > 5:
    print('Favor digitar o número de 0 a 5')

else:
    if n1 == n:
        print('Parabéns você acertou')
    else:
        print('Que pena tente outra vez')
        print('Numero sorteado: {}'.format(n1))