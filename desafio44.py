''' Elabore um programa que calcule o valor a ser pago por um produto, considerando o
seu preço normal e condição de pagamento:

– à vista dinheiro/cheque: 10% de desconto

– à vista no cartão: 5% de desconto

– em até 2x no cartão: preço formal

– 3x ou mais no cartão: 20% de juros'''


print('{:=^40}'.format('Lojas Guanabara'))
valor_compra= float(input('Preço das compras: '))
print('{:=^40}'.format('FORMAS DE PAGAMENTO:'))
print('{:40}'.format('1 - à vista dinheiro/cheque'))
print('{:40}'.format('2 – à vista no cartão'))
print('{:40}'.format('3 – em até 2x no cartão'))
print('{:40}'.format('4 – 3x ou mais no cartão'))

pagamento = float(input('Forma de pagamento: '))


if pagamento == 1:
        total = valor_compra - (valor_compra * 10/100)
elif pagamento ==2:
        total = valor_compra - (valor_compra * 5/100)
elif pagamento == 3:
        total = valor_compra
        print(f'Sua compra será parcelada em 2x de R$ {total/2:.2f} sem juros')
elif pagamento == 4:
        parcelas = int(input('Quantas parcelas: '))
        total = valor_compra + (valor_compra * 20/100)
        total_parcelado = total/parcelas

        print (f'Sua compra será parcelada em {parcelas}x de R$ {total:.2f} com juros')
else:
    print('Opção inválida de pagamento')

print(f'Sua compra de R$ {valor_compra:.2f} sairá por R$ {total:.2f}.')