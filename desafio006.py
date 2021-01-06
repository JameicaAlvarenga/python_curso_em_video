'''Crie um algoritimo que leia um numero e mostre o seu dobro, triplo e raiz quadrada '''

n = int(input('Digite um numero:'))
d = n * 2
t = n * 3
raiz = n **(1/2)
print('Numero digitaddo foi {}.'.format(n))
print('O dobro de {} vale : {} '.format(n,d))
print('O triplo é {}'.format(t))
print('A raiz quadrada é {:.2f}.'.format(raiz))
print('A raiz quadrada é {:.2f} '.format(pow(n,(1/2))))