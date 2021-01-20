'''
Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.
'''

nome = str(input('Digite o nome: ')).strip()
nome.upper().find('SILVA') == True
print('Tem Silva no nome')