'''Faça um programa que leia a largura e altrua em metros
Calcule a sua area e a quantidade de tinta necessária para pintá-la.
sabendo que cada litro de tinat pinta uma area de 2m²'''

l=float(input('Digite a Largura da parede: '))
a=float(input('Digite a altura da parede: '))
print('Total de área a ser pintada: {:.2f} m²'.format(l*a) )
print('Logo voce vai precisar de {:.2f} litros de tinta'.format((l*a)/2))