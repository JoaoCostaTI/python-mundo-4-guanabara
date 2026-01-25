# Declaração de Classe
class Gafanhoto:
    '''
    Docstring for Gafanhoto
    Essa classe cria um gafanhoto que é uma pessoa que tem nome e idade.
    Para criar uma nova pessoa, use
    variavel = Gafanhoto(nome, idade)
    '''
    def __init__(self, nome = "Vazio", idade = 0):
        # Atributos de intancia
        self.nome = nome
        self.idade = idade

    def __repr__(self):
        return f"{self.nome} é Gafanhoto e tem {self.idade} anos de idade"

    #Métodos de Instancia
    def aniversario(self):
        self.idade += 1
    
    def __getstate__(self):
        return f'Estado = Nome: {self.nome}, idade: {self.idade}'

# Declaração de Objetos
g1 = Gafanhoto('Joao', 32)
#print(g1.mensagem())
#print(g1)
#print(g1.__doc__)
print(g1.__dict__) # Atributo
print(g1.__getstate__()) # Metodo
print(g1.__class__)
