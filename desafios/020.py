from rich import print
from rich.panel import Panel

class Gamer:
    def __init__(self, nome, nick):
        self.nome = nome
        self.nick = nick
        self.lista_jogos = []
    def ficha(self):
        tabela = ''
        for j in self.lista_jogos:
            texto = f'[blue]- {j}[/]\n'
            tabela += texto
        mostrar_ficha = Panel(f'Nome Real: [blue]{self.nome}[/]\nJogos Favoritos:\n{tabela}', title=f'[white] Jogador <{self.nick}>[/]', width=35)
        print(mostrar_ficha)
        
        
    def add_favorito(self, jogo_favorito):
        self.lista_jogos.append(jogo_favorito)

j1 = Gamer('João Costa', 'Tevildo')
j1.add_favorito('Age of Empires')
j1.add_favorito('GTA 6')
j1.add_favorito('FIFA')
j1.ficha()

j2 = Gamer('Olivia Souza', 'peach_raivosa')
j2.add_favorito('Mario Bros')
j2.add_favorito('Call of Duty')
j2.ficha()