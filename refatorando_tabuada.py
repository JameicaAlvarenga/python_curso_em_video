"Tabuada "
import self as self

print('=' * 100, '\nGERADOR DE TABUADA\n', '=' * 100)
print('1: Soma')
print('2: Subtração')
print('3: Multiplicação')
print('4: Divisão')
print('5: Todas')
op = int(input('Escolha a operação:'))
n = int(input("Escolha um numero para gerar a tabuada:"))
a = 11


class Tabuada:
    def __init__(self, n):
        self.num_tabuada = n

    def soma(self):
        print('\nSoma:\n')
        for i in range(a):
            print('{:2} + {:2} = {}'.format(self.num_tabuada, i, self.num_tabuada + i))

    def subtracao(self):
        print('\nSubtração:\n')
        for i in range(a):
            print('{:2} - {:2} = {}'.format(self.num_tabuada + i, self.num_tabuada,
                                            (self.num_tabuada + i) - self.num_tabuada))

    def divisao(self):
        print('\nDivisão::\n')
        j = 0
        for i in range(1, a):
            print('{:2} / {:2} = {}'.format((self.num_tabuada + j), self.num_tabuada,
                                            (self.num_tabuada + j) / self.num_tabuada))
            j += self.num_tabuada

    def multiplicacao(self):
        print('\nMultiplicação:\n')
        for i in range(a):
            print('{:2} * {:2} = {}'.format(self.num_tabuada, i, (self.num_tabuada * i)))


tabuada = Tabuada(n)

if op == 1:
    tabuada.soma()

elif op == 2:
    tabuada.subtracao()

elif op == 3:
    tabuada.multiplicacao()

elif op == 4:
    tabuada.divisao()

elif op == 5:
    tabuada.soma()
    tabuada.subtracao()
    tabuada.multiplicacao()
    tabuada.divisao()
