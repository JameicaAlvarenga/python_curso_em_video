'''
Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem
dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.
'''



km = float(input("Quala a velocidade do carro?"))

if km <= 80 :
    print("Tenha um bom dia! Dirija com segurança!")
else:
    multa= (km-80)* 7
    print(f"MULTADO!! Excedeu o limite de 80Km/h! Multa de R$ {multa:.2f}")