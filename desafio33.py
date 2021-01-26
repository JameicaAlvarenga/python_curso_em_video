'''Faça um programa que leia três números e mostre qual é o maior e qual é o menor.'''
n1= input("Digite primeiro valor: ")
n2= input("Digite segundo valor: ")
n3= input("Digite terceiro valor: ")

##Menor valor
if n1 < n2 and n1< n3:
    menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n2 and n3 < n1:
    menor = n3

##Maior valor
if n1 > n2 and n1> n3:
    maior= n1
if n2 > n1 and n2 > n3:
    maior= n2
if n3 > n2 and n3 > n1:
    maior = n3
print(f'O maior valor digitado foi:{maior}')
print(f'O menor valor digitado foi:{menor}')
