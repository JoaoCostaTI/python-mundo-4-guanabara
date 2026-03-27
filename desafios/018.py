'''
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
        texto_analise = f'Analisando [green]{self.titulo}[/] com [blue]{self.qtd_pessoas} convidados[/]\nCada participante comerá {Churrasco.consumo_padrao}Kg e cada Kg custa R${Churrasco.preco_kg_carne:.2f}\nRecomendo [blue]comprar[/] [green]{self.qtd_carne:.3f}Kg[/] de carne\nO custo total será de [green]R${self.custo_total:.2f}[/]\nCada pessoa pagará [yellow]R${self.preco_por_pessoa:.2f}[/] para participar'

        analise_churrasco = Panel(texto_analise, title=self.titulo, style='white', width=60)
        print(analise_churrasco)

c1 = Churrasco('Churras dos Amigos', 15)
c1.analise()
'''

from rich import print
from rich.panel import Panel

class Churrasco:
    #Atributos de Classe
    consumo_padrao:float = 0.400
    preco_kg:float = 82.40

    def __init__(self, titulo, quant):
        #Atributos de Instancia
        self.titulo = titulo
        self.participantes = quant

    def calcular_qtd_carne(self)->float:
        return self.participantes * Churrasco.consumo_padrao

    def calcular_custo_total(self)->float:
        return self.calcular_qtd_carne() * self.__class__.preco_kg

    def calcular_custo_individual(self)->float:
        return self.calcular_custo_total() / self.participantes
    
    def __str__(self):
        return f"Esse é o {self.titulo} com {self.participantes} pessoas participantes"

    def analisar(self):
        conteudo = f'Analisando {self.titulo} com {self.participantes} convidados'
        conteudo += f'\nCada participante comerá {Churrasco.consumo_padrao}Kg e cada Kg custa R${Churrasco.preco_kg:,.2f}'
        conteudo += f'\nRecomendo comprar {self.calcular_qtd_carne():.3f}Kg de carne'
        conteudo += f'\nO custo total será de R${self.calcular_custo_total():,.2f}'
        conteudo += f'\nCada pessoa pagará R${self.calcular_custo_individual():,.2f} para participar'
        painel = Panel(conteudo, title=self.titulo)
        print(painel)

c1 = Churrasco('Churras dos Amigos', 15)
c1.analisar()

c2 = Churrasco('Festa do fim de ano', 80)
c2.analisar()
