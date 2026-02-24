from rich import print

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
        print(f'Você avançou {paginas_avancadas} páginas e agora está na [yellow]página {self.pagina_atual}[/]')
        


l1 = Livro('10 Coisas que aprendi', 20)
l1.avancar_paginas(5)
l1.avancar_paginas(10)
l1.avancar_paginas(100)
 