# - Exercício 1: Exercício de Classe, Atributo e Método (Nível Básico): Conta Bancária

# Você está criando um programa para representar contas bancárias. Cada conta bancária tem um número de conta, um titular da conta e um saldo. Você precisa criar uma classe ContaBancaria para representar essas contas e fornecer métodos para realizar operações básicas, como depósito e saque.

#qual a classe: conta_bancaria
#quais os atributos: num de conta, titular de conta, saldo
#quais os métodos: depositos e saques

class ContaBancaria:
        #sempre começar com o __init__ pois ele é o método contrutor (construir algo). 
    def __init__(self, num_conta, titular_conta):
        self.num_conta = num_conta
        self.titular_conta = titular_conta
        #saldo não entra nos atributos (lá em cima) pois ela inicia em zero
        self.saldo = 0.0 #desse jeito é mais seguro, pois temos certeza que vai iniciar com zero. 
            #outra maneira seria: 
                #def __init__(self, num_conta, titular_conta, saldo = 0):
                    #self.num_conta = num_conta
                    #self.titular_conta = titular_conta
                    #self.saldo = saldo -> mas aqui poderá haver erros de no futuro ter saldo e não ser zero.
    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f'Depósito de R${valor} realizado com sucesso.')
        else:
            print('O valor do depósito deve ser maior que zero.')

    def sacar(self, valor): 
        if valor > 0:
            if self.saldo >= valor:
                self.saldo -= valor
                print(f'Saque de R${valor} realizado com sucesso.')
            else:
                print('Saldo insuficiente para realizar o saque.')
        else:
            print('O valor do saque deve ser maior que zero.')

    def consultar_saldo(self):
            print(f'Saldo atual da conta de {self.titular_conta}: R${self.saldo}')
                        #self.num_conta / #self.titular_conta
conta1 = ContaBancaria(int(input("Número de conta: ")),input("Nome do titular de conta: "))
conta1.consultar_saldo()  # Saldo atual da conta de Thaysa Lima: R$0 -> pois o valor inicial de saldo é zero.

conta1.depositar(float(input("Colocar o valor que deseja depositar, que seja positivo por favor! \n")))
conta1.consultar_saldo()  

conta1.sacar(float(input("Colocar o valor que deseja sacar, que seja positivo por favor! \n"))) 
conta1.consultar_saldo()  


