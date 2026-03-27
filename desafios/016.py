"""
from rich import print

class Funcionario:

    empresa = 'Curso em video'

    def __init__(self, nome, setor, cargo):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo
    
    def apresentacao(self)->str:
        return f":smile: Olá, sou [blue]{self.nome}[/] e sou {self.cargo} do setor de {self.setor} da empresa {Funcionario.empresa}"

c1 = Funcionario('Maria', 'Administração', 'Diretora')
print(c1.apresentacao())

c2 = Funcionario('João', 'TI', 'Programador Python')
print(c2.apresentacao())
"""

from rich import print
from rich import inspect

class Funcionario:
    #Atributos de Classe
    empresa = 'Curso em Video'

    def __init__(self, nome, setor, cargo):
        #Atributos de instancia
        self.nome = nome
        self.setor = setor
        self.cargo = cargo
    
    def apresentacao(self)->str:
        return f":handshake: Olá, sou [blue]{self.nome}[/] e sou {self.cargo} do setor de {self.setor} da empresa {self.__class__.empresa}"

#Funcionario.empresa = 'Fiemg'        

c1 = Funcionario('Maria', 'Administração', 'Diretora')
c1.empresa = 'Estudonauta'
c1.salario = 9800
print(c1.salario)
print(c1.empresa)
inspect(c1)
print(c1.apresentacao())

c2 = Funcionario('João', 'TI', 'Programador Python')
inspect(c2)
print(c2.apresentacao())
inspect(Funcionario)