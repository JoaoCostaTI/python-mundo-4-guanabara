import tkinter as tk
from tkinter import ttk, messagebox

class ContaBancaria:
    '''
    Docstring for ContaBancaria
    Cria uma conta bancária e permite fazer saques e depósitos
    '''
    def __init__(self, id, nome_pessoa, saldo = 0):
        self.id = id
        self.titular = nome_pessoa
        self.saldo = saldo
        print(f'Conta: {self.id} criada com Sucesso!. Saldo Atual: R${self.saldo:,.2f}')
    
    def __repr__(self):
        return f"A conta {self.id} de {self.titular} tem R$ {self.saldo:,.2f} de saldo"
    
    def deposito(self, valor):
        self.saldo += valor
        print(f'Deposito autorizado com valor R$ {valor:,.2f}, na conta {self.id}')

    def saque(self, valor):
        if valor > self.saldo:
            messagebox.showwarning('Saldo insuficiente!', f'Valor R${valor:,.2f} indisponível! Saque NEGADO!')
            return
        self.saldo -= valor
        print(f'Saque autorizado com valor R$ {valor:,.2f}, na conta {self.id}')

    

conta_1 = ContaBancaria(112, 'João Costa', 3000)
conta_1.deposito(500)
conta_1.saque(200000)
print(conta_1)