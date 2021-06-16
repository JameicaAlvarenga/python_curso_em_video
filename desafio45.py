'''Exercício Python 45: Crie um programa que faça o computador jogar Jokenpô com você.'''
import random
import time

comp = random.randint(1,3)


print('{:=^40}'.format('PEDRA, PAPEL, TESOURA'))
print('[ 1 ] PEDRA')
print('[ 2 ] PAPEL')
print('[ 3 ] TESOURA')

jogador = int(input('Qual a sua jogada? '))

time.sleep(1)
print('JÓ')
time.sleep(1)
print('KEN')
time.sleep(1)
print('PO')
time.sleep(1)


if comp == jogador:
    resultado = 'Empate'
elif comp == 1 and jogador == 2:
    resultado = 'jogador vence'
elif comp == 2 and jogador == 3:
    resultado = 'jogador vence'
elif comp == 3 and jogador == 1:
     resultado = 'jogador vence'
else:
    resultado = 'computador vence'


if comp == 1:
    compt='PEDRA'
elif comp == 2:
    compt='PAPEL'
elif comp == 3:
    compt='TESOURA'


if jogador == 1:
    joga ='PEDRA'
elif jogador == 2:
    joga ='PAPEL'
elif jogador == 3:
    joga ='TESOURA'

print('-='*100)
print(f'O computador  jogou {compt}')
print(f'O jogador jogou {joga}')
print('-='*100)
print(resultado.upper())

