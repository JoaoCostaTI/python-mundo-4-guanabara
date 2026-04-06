from rich import print
from rich.panel import Panel

class Amplificador:
    volume_maximo = 10
    volume_minimo = 0

    def __init__(self, volume = 3):
        self.ligado = False
        self.mute = False
        self.volume = volume
        self.volume_atual = self.volume

    def mostrar_amplificador(self):
        energia = f'{"[black on green]  [/]"} Ligado' if self.ligado else f'{"[black on red]  [/]"} Desligado'
        if self.mute:
            mudo = 'Ativado'
            self.volume = 'SOM MUTADO'
        else:
            mudo = 'Desligado'
            self.volume = self.volume_atual

        if self.ligado:
            conteudo = f'Estado atual: {energia}\nMute: {mudo}\nVolume atual: {self.volume}'
        else:
            conteudo = f':prohibited: O Amplificador está DESLIGADO!'
        amp = Panel(conteudo, title='Ampeg', width=40)
        print(amp)
    
    def liga_desliga(self):
        self.ligado = not self.ligado
    
    def muta_desmuta(self):
        if self.ligado:
            self.mute = not self.mute
    
    def aumentar_volume(self):
        if self.ligado:
            if self.volume_atual == Amplificador.volume_maximo:
                self.volume_atual = Amplificador.volume_maximo
            else:
                self.volume_atual += 1
    
    def diminuir_volume(self):
        if self.ligado:
            if self.volume_atual == Amplificador.volume_minimo:
                self.volume_atual = Amplificador.volume_minimo
            else:
                self.volume_atual -= 1
            
        
amp = Amplificador()

while True:
    amp.mostrar_amplificador()
    op = input('>>> ')
    match op:
        case '0':
            break
        case '@':
            amp.liga_desliga()
        case 'm':
            amp.muta_desmuta()
        case '+':
            amp.aumentar_volume()
        case '-':
            amp.diminuir_volume()