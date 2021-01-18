'''
Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
Faça um programa que ajude ele, lendo o nome  dos alunos e escrevendo na tela o nome do escolhido.
'''

import random

aluno_1 = input('Informe o nome do aluno: ')
aluno_2 = input('Informe o nome do aluno: ')
aluno_3 = input('Informe o nome do aluno: ')
aluno_4 = input('Informe o nome do aluno: ')

lista = [aluno_1,aluno_2,aluno_3,aluno_4]
aluno = random.choice(lista)
print ('O sortudo foi: {} '.format(aluno))

