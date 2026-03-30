from rich import print
"""
class Caneta:
    def __init__(self, cor):
        self.cor = cor
        self.tampada = False
    
    def destampar(self):
        self.tampada = True

    def escrever(self, texto):
        if self.tampada:
            print(f'[{self.cor}]{texto}[/]', end=' ')
            return
        print(f'A [blue]Caneta[/] está tampada')

    def quebrar_linha(self, n_linhas):
        for l in range(n_linhas):
            print()
        
c1 = Caneta('green')
c2 = Caneta('blue')
c3 = Caneta('red')

c1.destampar()
c2.destampar()
c3.destampar()
c1.escrever('Olá Mundo! ')
c1.quebrar_linha(2)
c2.escrever('Olá Gafanhoto!')
c3.escrever('Vamos exercitar! ')
"""
class Caneta:
    def __init__(self, cor = 'azul'):
        escolha = ''
        match cor.lower().strip():
            case 'azul':
                escolha = '[blue]'
            case 'verde':
                escolha = '[green]'
            case 'vermelho' | 'vermelha':
                escolha = '[red]'
            case _:
                escolha = '[white]'

        self.tampada = True

        self.cor = escolha

    def escrever(self, msg):
        if self.tampada:
            print(f'A {self.cor}caneta[/] está tampada')
        else:
            print(f'{self.cor}{msg}[/]', end=' ')

    def quebrar_linha(self, n_linhas = 1):
        print('\n' * n_linhas, end='')

    def tampar(self):
        self.tampada = True

    def destamapar(self):
        self.tampada = False

c1 = Caneta('azul')
c2 = Caneta('vermelha')
c3 = Caneta('verde')

c1.destamapar()
c2.destamapar()
c3.destamapar()

c1.escrever('Olá Mundo')
c2.escrever('Funciona')
c2.quebrar_linha(2)
c3.escrever('Deu certo!')

#c1.tampar()
c3.quebrar_linha(5)
c1.escrever('Será q rola')