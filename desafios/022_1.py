from rich import print
from rich.panel import Panel

class ControleRemoto:
    canal_min = 1
    canal_max = 6
    volume_min = 1
    volume_max = 5

    def __init__(self, canal = 1, volume = 3):
        self.ligado = False
        self.canal_atual = canal
        self.volume_atual = volume

    def canal_mais(self):
        if self.ligado:
            if self.canal_atual < ControleRemoto.canal_max:
                self.canal_atual += 1
            else:
                self.canal_atual = ControleRemoto.canal_min
            
    def canal_menos(self):
        if self.ligado:
            self.canal_atual -= 1

    def mostrar_tv(self):
        conteudo = ''
        if not self.ligado:
            conteudo = ':prohibited:[red] A TV está desligada[/]'
        else:
            conteudo = 'CANAL = '
            for c in range(ControleRemoto.canal_min, ControleRemoto.canal_max + 1):
                if c == self.canal_atual:
                    conteudo += f' [black on yellow]{c}[/] '
                else:
                    conteudo += f" {c} "
            conteudo += '\nVOLUME = '
            for v in range(ControleRemoto.volume_min, ControleRemoto.volume_max + 1):
                if v <= self.volume_atual:
                    conteudo += '[black on purple][][/]'
                else:
                    conteudo += '[]'
        tv = Panel(conteudo, title='[ TV ] ', width=35)
        print(tv)
           
    def liga_desliga(self):
        self.ligado = not self.ligado


c1 = ControleRemoto(canal=3, volume=4)
c1.liga_desliga()
c1.mostrar_tv()
c1.canal_mais()
c1.canal_mais()
c1.canal_mais()
c1.canal_mais()
c1.canal_mais()

c1.mostrar_tv()

