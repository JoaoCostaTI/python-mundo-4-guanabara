# Declaração de Classe
class Gafanhoto:
    def __init__(self):
        # Atributos de intancia
        self.nome = ""
        self.idade = 0

    #Métodos de Instancia
    def aniversario(self):
        self.idade += 1
    
    def mensagem(self):
        return f"{self.nome} é Gafanhoto e tem {self.idade} anos de idade"

# Declaração de Objetos
joao = Gafanhoto()
joao.nome = 'João'
joao.idade = 32
joao.aniversario()
joao.aniversario()
print(joao.mensagem())

maria = Gafanhoto()
maria.nome = 'Maria'
maria.idade = 52
maria.aniversario()
print(maria.mensagem())