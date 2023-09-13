class ContaBancária:
    def __init__(self, numero_conta, titular):
        self.numero_conta = numero_conta
        self.titular = titular
        self.saldo = 0.0

    def depositar(self, valor):
        if valor > 0:
            self.saldo =+ valor #self.saldo = self.saldo + valor
            print(f'Valor depositado de R${valor}, realizado com sucesso')
        else:
            print('O valor do depósito deve ser maior que 0')

    def sacar(self, valor):
        if valor > 0:
            if self.saldo >= valor:
                self.saldo -= valor
                print(f'Saque de R${valor} realizado com sucesso')
            else:
                print('Saldo insuficiente para realizar o saque')
        else:
            print('O valor deve ser maior que 0')

conta = ContaBancária(202301, "Natalia Rosa")

conta.depositar(100)

conta.sacar(20)

print(conta.saldo)

contaLais = ContaBancária(202302, "Lais")

contaLais.depositar(80)

contaLais.sacar(1000)



        