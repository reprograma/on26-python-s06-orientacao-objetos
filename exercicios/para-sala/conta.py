class contaBancaria:
    def __init__ (self, numeroDaConta, titularConta):
        self.numeroDaConta = numeroDaConta
        self.titularConta = titularConta
        self.saldo = 0.0

    def depositar(self, valor):
        if valor > 0:
            self.saldo =+ valor
            print(f'Depósito de R${valor} realizado com sucesso.')
        else:
            print('O valor do depósito deve ser maior que 0.')

    def sacar(self, valor):
        if valor > 0:
            if self.saldo >= valor:
                self.saldo -= valor
                print(f"Saque de R${valor} realizado com sucesso.")
            else:
                print(f"Saldo insuficiente. Saque até R${self.saldo}.")
        else:
            print("O valor do saque deve ser maior que 0.")

conta = contaBancaria(202301, "Maria Leandro")


conta.depositar(100)
conta.sacar(50)
print(conta.saldo)



    
    