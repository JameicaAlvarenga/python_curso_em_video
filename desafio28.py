'''
Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e
peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
O programa deverá escrever na tela se o usuário venceu ou perdeu.


'''

import random

print('Adivinha em que número de 0 a 5 estou pensando?' )


n1=random.randint(0,5)
n= int(input('Digite um valor de 0 a 5: '))
if n > 5:
    print('Favor digitar o número de 0 a 5')

else:
    if n1 == n:
        print('Parabéns você acertou')
    else:
        print('Que pena tente outra vez')
        print('Numero sorteado: {}'.format(n1))