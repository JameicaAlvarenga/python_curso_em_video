''': Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar
o tempo que falta ou que passou do prazo.'''
from datetime import date

ano = int(input('Ano de Nascimento: '))

data =date.today().year

idade = data - ano

if idade < 18:
    print('Quem nasceu no ano de {}, possui {} e faltam {} anos para se alistar'.format(ano, idade,18-idade))
    print('Seu alistamento será no ano de {}'.format(data+(18-idade)))

elif idade > 18:
    print('Quem nasceu no ano de {}, possui {} e ja deveria ter se alitado a {} anos'.format(ano, idade,idade-18))
else:
    print('Quem nasceu no ano de {}, possui {} e esta pronto para se alistar'.format(ano, idade))


