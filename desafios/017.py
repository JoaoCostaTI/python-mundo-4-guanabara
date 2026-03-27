'''
from rich import print
from rich.panel import Panel
from rich.align import Align

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def etiqueta(self):
        texto_etiqueta = f'{self.nome}\n------------\nR${self.preco:,.2f}'
        texto_centralizado = Align.center(texto_etiqueta)

        etiqueta_produto = Panel(texto_centralizado, title='Produto', style='white', width=35)
        print(etiqueta_produto)

p1 = Produto('Iphone 17 PRO MAX', 25_000.85)
p2 = Produto('Notebook Gamer', 8_000)

p1.etiqueta()
p2.etiqueta()
'''

from rich import print
from rich.panel import Panel

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
    
    def __str__(self):
        return f'{self.nome} custa R${self.preco:,.2f}'
    
    def etiqueta(self):
        conteudo = f"{self.nome.center(30,' ')}"
        conteudo += f"{'-' * 30}"
        precof = f"R${self.preco:,.2f}"
        conteudo += f"{precof.center(30, '.')}"
        etiqueta = Panel(conteudo, title='Produto', width=34)
        print(etiqueta)

p1 = Produto('Iphone 17 Pro Max', 25_000.85)
p1.etiqueta()

p2 = Produto('Notebook Gamer', 8000)
p2.etiqueta()


