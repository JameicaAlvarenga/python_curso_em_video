'''Leia o salario de um funcionário e  mostre o seu novo salario com aumento de 15%'''

salario = float(input('Informe o salário: R$'))
aumento = float(input('Informe o percentual de aumento: '))
reajuste= salario + (salario * aumento/100)
print ('O salario passou de R$ {:.2f} para R$ {:.2f}'.format(salario,reajuste))