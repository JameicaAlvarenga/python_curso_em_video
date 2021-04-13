'''A Confederação Nacional de Natação precisa de um programa que leia o ano de
nascimento de um atleta e mostre sua categoria, de acordo com a idade:

– Até 9 anos: MIRIM

– Até 14 anos: INFANTIL

– Até 19 anos: JÚNIOR

– Até 25 anos: SÊNIOR

– Acima de 25 anos: MASTER'''

from datetime import date

ano = int(input('Informe o ano de nascimento: '))
'''data = date.today().year'''
idade = (date.today().year - ano)


if idade <= 9:
    print(f'Você possui {idade} anos se encaicxa na categoria Mirim')
elif 9 > idade <= 14:
    print(f'Você possui {idade} anos se encaicxa na categoria Infantil')
elif 14 > idade <= 19:
    print(f'Você possui {idade} anos se encaicxa na categoria Júnior')
elif 19 > idade <= 25:
    print(f'Você possui {idade} anos se encaicxa na categoria Sênior')
else:
    print(f'Você possui {idade} anos se encaicxa na categoria Master')
