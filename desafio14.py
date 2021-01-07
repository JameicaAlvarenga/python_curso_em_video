'''Conversor de Celsius para Fahrenheit'''

def fahrenheit_celsius (c):
    return (c - 32) * 5 / 9

def celsius_fahrenheit(c):
    return (c * 9 / 5) + 32


if __name__=='__main__':

    n = float(input('Informe o valor que deseja converter: ' ))
    t = input('Escolha o tipo de conversão:\n 1 - Celsius_Fahrenheit \n 2 - Fahrenheit_Celsius \n')

    if t == '1':
        print('Opção 1: Então {:.2f}º Celsius corresponde a {:.2f}º Fahrenheit.'.format(n, celsius_fahrenheit (n)))
    elif t == '2':
        print('Opção 2: Então {:.2f}º Fahrenheit corresponde a {:.2f}º Celsius.'.format(n, fahrenheit_celsius(n)))


