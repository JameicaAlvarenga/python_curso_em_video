"Tabuada "

print('1: Soma')
print('2: Subtração')
print('3: Multiplicação')
print('4: Divisão')
print('5: Todas')
op = int(input('Escolha a operação:'))
n = int(input("Digite um numero:"))
a = 11

def soma (n):
    for i in range(a):
        print('{:2} + {:2} = {}'.format(n, i, n + i))

def subtracao(n):
    for i in range(a):
        print('{:2} - {:2} = {}'.format(n+i, n, (n+i) - n))

def divisao(n):
    j = 0
    for i in range(1, a):
        print('{:2} / {:2} = {}'.format((n + j), n, (n + j) / n))
        j += n

def multiplicacao(n):
    for i in range(a):
        print('{:2} * {:2} = {}'.format(n, i, (n * i)))


if op == 1:
    soma(n);

elif op == 2:
    subtracao(n);

elif op == 3:
    multiplicacao(n);

elif op == 4:
   divisao(n);

elif op == 5:
    soma(n)
    subtracao(n)
    multiplicacao(n)
    divisao(n)
