'''Conversor de Celsius para Fahrenheit'''


def fahrenheit_celsius (c):
    return  (c * 9/5) + 32

if __name__=='__main__':

    n = float(input('Informe o valor do grau Celsius: ' ))

    print('{:.2f}º Celsius corresponde a {:.2f}º Fahrenheit.'.format(n, fahrenheit_celsius(n)))