'''Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário
escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.'''

n = int(input('Digite um numero: '))
op = input('Escolha a opção: '
           '1 - Binário '
           '2 - Octadecimal '
           '3 - Hexadecimal ')

if op == '1':
    print(f'o numero, {n} convertido em Binário é: {bin(n)}')

if op == '2':
    print(f'o numero, {n} convertido em Binário é: {oct(n)}')

if op == '3':
    print(f'o numero, {n} convertido em Binário é: {hex(n)}')







