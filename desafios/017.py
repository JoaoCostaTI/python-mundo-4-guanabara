from rich import print
from rich.panel import Panel
from rich.align import Align

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def etiqueta(self):
        texto_etiqueta = f'{self.nome}\n------------\nR${self.preco:.2f}'
        texto_centralizado = Align.center(texto_etiqueta)

        etiqueta_produto = Panel(texto_centralizado, title='Produto', style='white', width=35)
        print(etiqueta_produto)

p1 = Produto('Iphone 17 PRO MAX', 25000.85)
p2 = Produto('Mouse', 120)

p1.etiqueta()
p2.etiqueta()