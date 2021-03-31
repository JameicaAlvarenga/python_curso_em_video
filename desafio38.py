''' Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:

– O primeiro valor é maior

– O segundo valor é maior

– Não existe valor maior, os dois são iguais'''

n1 = int(input('informe o numero: '))
n2 = int(input('informe o numero: '))

if n1 == n2:
    print('Não existe valor maior, os dois são iguais')

elif n1 > n2 :
    print('O primeiro valor é maior')

else:
    print('O segundo valor é maior')