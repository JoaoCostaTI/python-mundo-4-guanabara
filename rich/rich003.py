from rich import print
from rich.table import Table

tabela = Table(title='Tabela de Preços')

tabela.add_column('Nome')
tabela.add_column('Preço')

tabela.add_row('Lápis', '1,50')
tabela.add_row('Borracha', '0,50')

print(tabela)