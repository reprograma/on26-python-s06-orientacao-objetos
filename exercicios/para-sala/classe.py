''' 
Exercicio de classe, atributo e método: conta bancária

Você está criando um programa para representar contas bancárias.
Cada conta bancária tem um número de conta e um saldo.
Você precisa criar uma classe contaBancaria para representar essas contas e fornecer métodos
para realizar operações básicas, como depósito e saque.
'''

class contaBancaria:
    def __init__(self, numero_conta, titular_conta):
        self.numero_conta = numero_conta
        self.titular_conta = titular_conta
        self.saldo = 0.0    # saldo inicial definido com 0.0
    
    def depositar(self, valor):
        if valor > 0:
            self.saldo =+ valor    # self.saldo = self.saldo + valor
            print(f'Valor de R${valor} depositado com sucesso!')
        else:
            print('O valor do depósito deve ser maior que 0')
    
    def sacar(self, valor):
        if valor > 0:
            if self.saldo >= valor:
                self.saldo -= valor
                print(f'Saque de R${valor} realizado com sucesso!')
            else:
                print('saldo insuficiente para realizar o saque')
        else:
            print('o valor do saque deve ser maior que 0')

contaJessica = contaBancaria(202301, "Jéssica Machado")
contaJessica.depositar(100)
contaJessica.sacar(10)
print(f'Saldo disponível: R${contaJessica.saldo}')

contaLais = contaBancaria(202302, "Lais")
contaLais.depositar(500)
contaLais.sacar(100)

