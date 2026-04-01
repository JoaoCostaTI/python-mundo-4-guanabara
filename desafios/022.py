from rich import print
from rich.panel import Panel

class ControleRemoto:
    canal_min = 1
    canal_max = 5
    vol_min = 1
    vol_max = 5

    def __init__(self, canal = 1, volume = 3):
        self.canal_atual = canal
        self.volume_atual = volume
        self.ligado = False

    def liga_desliga(self):
        self.ligado = not self.ligado

    def canal_mais(self):
        if self.ligado:
            if self.canal_atual == ControleRemoto.canal_max:
                self.canal_atual = ControleRemoto.canal_min
            else:
                self.canal_atual += 1
    def canal_menos(self):
        if self.ligado:
            if self.canal_atual == ControleRemoto.canal_min:
                self.canal_atual = ControleRemoto.canal_max
            else:
                self.canal_atual -= 1
    def volume_mais(self):
        if self.ligado:
            if self.volume_atual == ControleRemoto.vol_max:
                self.volume_atual = ControleRemoto.vol_max
            else:
                self.volume_atual += 1
    def volume_menos(self):
        if self.ligado:
            if self.volume_atual == ControleRemoto.vol_min:
                self.volume_atual = ControleRemoto.vol_min
            else:
                self.volume_atual -= 1

    def mostra_tv(self):
        conteudo = ""
        if not self.ligado:
            conteudo = f':prohibited: [red]A TV está desligada![/] '
        else:
            conteudo = f'CANAL = '
            for canal in range(ControleRemoto.canal_min, ControleRemoto.canal_max + 1):
                if canal == self.canal_atual:
                    conteudo += f' [black on yellow] {canal} [/] '
                else:
                    conteudo += f' {canal} '
            
            conteudo += f'\nVOLUME = '
            for volume in range(ControleRemoto.vol_min, ControleRemoto.vol_max +1):
                if volume <= self.volume_atual:
                    conteudo += f'[black on cyan] [/]'
                else:
                    conteudo += f'[black on white] [/]'
        tv = Panel(conteudo, title='[ TV ]', width=35)
        print(tv)

c = ControleRemoto()
while True:
    c.mostra_tv()
    comando = str(input(f'[< CH >   - VOL +] :'))
    match comando:
        case '0':
            break
        case '@':
            c.liga_desliga()
        case'>':
            c.canal_mais()
        case'<':
            c.canal_menos()
        case'+':
            c.volume_mais()
        case'-':
            c.volume_menos()




