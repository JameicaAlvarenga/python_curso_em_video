"Tabuada "

print('1: Soma')
print('2: Subtração')
print('3: Multiplicação')
print('4: Divisão')
op = int(input('Escolha a operação:'))
n = int(input("Digite um numero:"))
a = 11

if op == 1:
    for i in range(a):
        print('{} + {} = {}'.format(n, i, n + i))
elif op == 2:
    for i in range(a):
        print('{} - {} = {}'.format(n+i, n, (n+i) - n))
elif op == 3:
    for i in range(a):
        print('{} * {} = {}'.format(n, i, n * i))
elif op == 4:
    j = 0
    for i in range(1, a):
        print('{} / {} = {}'.format((n+j), n, (n+j) / n))
        j += n
