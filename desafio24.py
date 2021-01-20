'''
 Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.
'''

cidade = input('Digite a cidade: ').strip()

if cidade[:5].upper() == 'SANTO':
    print ('A cidade começa com Santo')
else:
    print ('A cidade não começa com Santo')
