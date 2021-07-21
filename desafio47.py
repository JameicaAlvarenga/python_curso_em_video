'''Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.

'''

for n in range(1,51):
    if n%2 == 0:
        print(n, end=' ')

for n in range(2,51,2):
    print(n)


print('\nDesafio48: Faça um programa que calcule a soma entre todos os números impares que são múltiplos '
      'de três e que se encontram no intervalo de 1 até 500.')
soma=0
qtd=0
for n in range (1,501, 2):
    if  n%3==0:
        qtd+=1
        print(n, end=" ")
        soma+=n
print('\nA soma entre esses valores é:{}'.format(soma))
print(f'Foram somados:{qtd}')