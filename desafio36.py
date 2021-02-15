'''Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal
não pode exceder 30% do salário ou então o empréstimo será negado.'''

casa = float(input('Valor da casa: '))
salario = float(input('Qual o salario do comprador: '))
anos =  int(input("Em quantos anos deseja parcelar o valor da casa? "))

parc_min = (salario * 30/100)
prestacao = casa/(anos*12)

if prestacao > parc_min :
 print('Emprestimo Negado devido politicas de crédito')
else:
    print(f'Emprestimo liberado. Serão {anos*12:.2f} parcelas, no valor de {prestacao :.2f} cada')


