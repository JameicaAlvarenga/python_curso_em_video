'''Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade
de dia pelos quais ele foi alugado.
Calcule ao preço a pagar, sabendo que o carro custa R$ 60,00 por dia e R$ 0,15 por km'''

dias = int(input('Quantos dias de aluguel: '))
km = float(input('Qual a distancia percorrida em Km: '))

total_a_pagar = (dias * 60) + (km * 0.15)

print('Valor total a pagar : R$ {:.2f}'.format(total_a_pagar))
