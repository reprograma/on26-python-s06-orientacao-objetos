class conta:
    def __init__(self, numero, titular_conta, saldo): # metodo construtor
        self.numero = numero
        self.titular_conta = titular_conta
        self.saldo = 0.0

    def depositar(self, valor):
        if valor > 0:
            self.saldo =+ valor
            print(f'Valor depositado de R${valor} realizado com sucesso.')
        else:
            print('O valor do depósito deve ser maior que zero.')
    
    def sacar(self, valor):
        if valor > 0:
            if self.saldo >= valor
            self.saldo -= valor
            print(f'Saque de R$ {valor} realizado com sucesso.')
        else:
            print(f'O valor do seu saldo deve ser maior que o valor de saque. Seu saldo é de {saldo}')
        
conta = conta(202301, 'Daviny Letícia')

conta.depositar(100)