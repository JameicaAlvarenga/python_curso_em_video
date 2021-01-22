'''
 Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”,
 em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
'''

texto = str(input('Digite o texto desejado:')).strip()
print('O texto digitado possui {} letras A.'.format(texto.upper().count('A',0,len(texto))))
print('A primeira letra A está na posição numero : {}'.format(texto.upper().index('A')))
print('A ultima  letra a está na posição numero : {}'.format(texto.upper().rfind('A')+1))