'''Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que
 forem pares. Se o valor digitado for ímpar, desconsidere-o.'''
lista = []
for n in range(1, 7):
    numero = int(input("Dgigite um  numero inteiro: "))
    if numero % 2 == 0:
        lista.append(numero)

print(lista)
print('Soma dos valores é :', sum(lista))
