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
            if self.canal_atual > ControleRemoto.canal_min:
                self.canal_atual -= 1
            else:
                self.canal_atual = ControleRemoto.canal_max

    def volume_mais(self):
        if self.ligado:
            if self.volume_atual < ControleRemoto.volume_max:
                self.volume_atual += 1
            else:
                self.volume_atual = ControleRemoto.volume_max    

    def volume_menos(self):
        if self.ligado:
            if self.volume_atual > ControleRemoto.volume_min:
                self.volume_atual -= 1
            else:
                self.volume_atual = ControleRemoto.volume_min

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
                    conteudo += '[black on purple]   [/]'
                else:
                    conteudo += '[black on white]   [/]'
        tv = Panel(conteudo, title='[ TV ] ', width=35)
        print(tv)
           
    def liga_desliga(self):
        self.ligado = not self.ligado


c1 = ControleRemoto()

while True:
    c1.mostrar_tv()
    escolha = str(input(f'< CH {c1.canal_atual} >  - VOL {c1.volume_atual} + '))
    match escolha:
        case '0':
            break
        case '@':
            c1.liga_desliga()
        case '>':
            c1.canal_mais()
        case '<':
            c1.canal_menos()
        case '-':
            c1.volume_menos()
        case '+':
            c1.volume_mais()
