from rich import print
from rich.panel import Panel

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
    
    def mostrar_produto(self):
        produto = f'Nome: {self.nome}\nPreço: R${self.preco:.2f}'
        Visor(produto)
        
    
class ProdutoPerecivel(Produto):
    def __init__(self, nome, preco, data_validade):
        super().__init__(nome, preco)
        self.data_validade = data_validade

    def mostrar_produto(self):
        produto = f'Nome: {self.nome}\nPreço: R${self.preco:.2f}\nValidade: {self.data_validade}'
        Visor(produto)

class Visor:
    def __init__(self, produto):
        p = Panel(produto, title='Produto', width=30)
        print(p)

p1 = Produto('Pera', 18)
p1.mostrar_produto()

p2 = ProdutoPerecivel('Ovo', 29, '18/06/2026')
p2.mostrar_produto()


