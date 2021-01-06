'''Crie um programa que leia quanto de dinheiro uma pessoa tem na carteira e
 quanto dolares ela pode comprar'''

import requests



def conversor_dolar (self):
    url = f'https://economia.awesomeapi.com.br/all/{self}'
    resp = requests.get(url)
    return resp.json()['USD']['high']

if __name__=='__main__':
    print('Valor do dolar hoje é:',conversor_dolar('USD-BRL'))
    n=float(input('Valor de dinheiro em carteira em reais é:'))
    print('Logo você pode comprar :{:.2f} dolares.'.format(n/float(conversor_dolar('USD-BRL'))))


