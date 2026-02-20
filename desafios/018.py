from rich import print
from rich.panel import Panel

class Churrasco:
    consumo_padrao = 0.4
    preco_kg_carne = 82.40
    def __init__(self, titulo,qtd_pessoas):
        self.qtd_carne = qtd_pessoas * Churrasco.consumo_padrao
        self.custo_total = self.qtd_carne * Churrasco.preco_kg_carne
        self.qtd_pessoas = qtd_pessoas
        self.preco_por_pessoa = self.custo_total / self.qtd_pessoas
        self.titulo = titulo
        
    
    def analise(self):
        #Quantidade de carne a ser comprado
        #Custo total do Churrasco
        #Preço por pessoa
        texto_analise = f'Analisando [green]{self.titulo}[/] com [blue]{self.qtd_pessoas} convidados[/]\nCada participante comerá {Churrasco.consumo_padrao}Kg e cada Kg custa R${Churrasco.preco_kg_carne:.2f}\nRecomendo [blue]comprar[/] [green]{self.qtd_carne:.3f}Kg[/] de carne\nO custo total será de [green]R${self.custo_total:.2f}[/]\nCada pessoa pagará [yellow]R${self.preco_por_pessoa:.2f}[/]'

        analise_churrasco = Panel(texto_analise, title=self.titulo, style='white', width=60)
        print(analise_churrasco)

c1 = Churrasco('Churras dos Amigos', 100)
c1.analise()