from rich import print

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

c1.escrever('Olá, Mundo!')
c1.quebrar_linha(4)
c2.escrever('Olá Gafanhoto!')
c3.escrever('Vamos exercitar')