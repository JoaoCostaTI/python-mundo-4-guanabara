from rich import inspect, print
from aluno import Aluno
from professor import Professor
from funcionario import Funcionario

def main():

    a1 = Aluno('Jose', 17, 'Informática', 'T01')
    a1.fazer_aniversario()
    a1.fazer_matricula()
    inspect(a1, methods=True)

    p1 = Professor('João', 32, 'Programador Python', 'Mestre')
    p1.fazer_aniversario()
    p1.dar_aula()
    inspect(p1, methods=True)

    f1 = Funcionario('Carla', 37, 'Bibliotecaria', 'Biblioteca')
    f1.fazer_aniversario()
    f1.bater_ponto()
    inspect(f1, methods=True)

if __name__ == '__main__':
    main()