from rich import print
from rich.panel import Panel

caixa = Panel('[white]Esse aqui é um painel de Exemplo[/]:+1:', title='Mensagem', style='red', width=35)

print(caixa)