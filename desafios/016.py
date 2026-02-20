from rich import print

class Funcionario:

    empresa = 'Curso em video'

    def __init__(self, nome, setor, cargo):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo
    
    def apresentacao(self):
        return f":smile: Olá, sou [blue]{self.nome}[/] e sou {self.cargo} do setor de {self.setor} da empresa {Funcionario.empresa}"

c1 = Funcionario('Maria', 'Administração', 'Diretora')
print(c1.apresentacao())

c2 = Funcionario('João', 'TI', 'Programador Python')
print(c2.apresentacao())