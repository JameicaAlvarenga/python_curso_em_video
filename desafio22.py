'''
Crie um programa que leia o nome completo de uma pessoa e mostre:

– O nome com todas as letras maiúsculas e minúsculas.

– Quantas letras ao todo (sem considerar espaços).

– Quantas letras tem o primeiro nome.
'''

nome = (input('Informe o nome completo:')).strip()

div_nome = nome.split()
tam = len(div_nome[0])
tot_letras = len(nome.replace(' ',''))

print('Letras maiusculas: {}'.format(nome.upper()))
print('Letras Minusculas: {}'.format(nome.lower()))
print('O nome digitado possui {} letras.'.format(tot_letras))
print('O primeiro nome tem {} letras.'.format(tam))
