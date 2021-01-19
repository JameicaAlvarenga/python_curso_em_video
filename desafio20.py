'''
O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos.
Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
'''

from random import shuffle

aluno_1 = input('Informe o nome do aluno: ')
aluno_2 = input('Informe o nome do aluno: ')
aluno_3 = input('Informe o nome do aluno: ')
aluno_4 = input('Informe o nome do aluno: ')

lista = [aluno_1,aluno_2,aluno_3,aluno_4]
shuffle(lista)
print('A ordem será:{}'.format(lista))
