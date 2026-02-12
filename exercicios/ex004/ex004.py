from rich import inspect

class ContaBancaria:
    '''
        Cria uma conta bancária e permite fazer saques e depósitos
    '''
    def __init__(self, id, nome, saldo):
        self.id = id
        self.titular = nome
        self.saldo = saldo
        print(f'Conta: {self.id} criada com sucesso!. Saldo Atual de R${self.saldo:.2f}')

    def __str__(self):
        return f"A conta {self.id} de {self.titular} tem R${self.saldo:.2f}"


conta = ContaBancaria(111, 'José', 500)

inspect(conta)
