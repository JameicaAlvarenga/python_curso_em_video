'''Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que
 forem pares. Se o valor digitado for ímpar, desconsidere-o.'''
lista = []
cont=0
for n in range(1, 7):
    numero = int(input("Dgigite um  numero inteiro: "))
    cont +=1
    if numero % 2 == 0:
        lista.append(numero)


print('Voce informou {} números e a soma dos números pares informados é :{}'.format(cont,sum(lista)))
