'''Calulando desconto de x% do produto e mostre o novo valor na tela'''

precoInicial = float(input('Qual o valor do produto: R$ '))
desconto =  float(input('Qual o valor do desconto: R$ '))
precoFinal = precoInicial - (precoInicial * desconto /100)

print('O valor do produto é {:.2f}, com o desconto de {:.2f}, o novo valor a ser pago é: R$ {:.2f}'.format(precoInicial,desconto,precoFinal))

