'''Faça um programa que leia um numero inteiro
 e mostre na tela o seu sucessor e seu antecessor '''

n1 = int(input('Digite um numero: '))
ant = n1 -1
suc = n1 + 1
print("O numero antecessor de {} é: {} e o sucessor é {}".format(n1, ant, suc))