'''
from rich import print
from time import sleep

class Livro:
    def __init__(self, titulo, n_paginas):
        self.titulo = titulo
        self.n_paginas = n_paginas
        self.total_paginas = self.n_paginas
        self.pagina_atual = 1
        self.apresentacao()
    
    def apresentacao(self):
        print(f'Você acabou de abrir o livro [red]"{self.titulo}"[/] que tem [green]{self.n_paginas}[/] páginas no total. Você agora está na [yellow]página {self.pagina_atual}[/]')

    def avancar_paginas(self, n_paginas):
        salto_paginas = self.pagina_atual + n_paginas
        paginas_avancadas = 0
        for p in range(self.pagina_atual+1,  salto_paginas+1):
            print(f'Pág {p} > ', end='')
            self.pagina_atual = p
            paginas_avancadas+=1
            if p >= self.total_paginas:
                print(f'Você avançou {paginas_avancadas} páginas e agora está na [yellow]página {self.pagina_atual}[/]')
                print(f'[red]Voce chegou ao final do livro "{self.titulo}"[/]')
                return
            sleep(0.2)
        print(f'Você avançou {paginas_avancadas} páginas e agora está na [yellow]página {self.pagina_atual}[/]')
        
l1 = Livro('10 Coisas que aprendi', 20)
l1.avancar_paginas(5)
l1.avancar_paginas(10)
l1.avancar_paginas(50)
'''
from rich import print
from time import sleep

class Livro:
    def __init__(self, titulo, paginas):
        self.titulo = titulo
        self.total_paginas = paginas
        self.pagina_atual = 1
        print(f':open_book: Você acabou de abrir o livro {self.titulo} que tem {self.total_paginas} páginas no total. Você agora está na página {self.pagina_atual}')

    def avancar_paginas(self, qtd=1):
        cont = 0
        for pg in range(0, qtd, 1):
            if not self.fim_do_livro():
                self.pagina_atual += 1
                print(f'Pág{self.pagina_atual} :arrow_forward:', end=' ')
                cont += 1
                sleep(0.2)

        print(f'Você avançou {cont} páginas, e agora está na página {self.pagina_atual}')
        if self.fim_do_livro():
            print(f':closed_book: Você chegou ao final do livro {self.titulo}')

    def fim_do_livro(self):
        if self.pagina_atual == self.total_paginas:
            return True
        return False
    
l1 = Livro('10 coisas que aprendi', 20)
l1.avancar_paginas(5)
l1.avancar_paginas(10)
l1.avancar_paginas(50)

