#Você está criando um programa para representar contas bancárias. Cada conta bancária tem um número de conta, um titular da conta e um saldo. Você precisa criar uma classe ContaBancaria para representar essas contas e fornecer métodos para realizar operações básicas, como depósito e saque.

class ContaBancaria:
        #sempre começar com o __init__ pois ele é o método contrutor (construir algo). 
    def __init__(self, num_conta, titular_conta): #entre parenteses vão os atributos
        self.num_conta = num_conta
        self.titular_conta = titular_conta
        self.saldo = 0.0 #Não é declarado como um dos atributos por começar com 0 

    def depositar(self, deposito): #Depositar é um método da classe ContaBancaria
        if deposito > 0:
            self.saldo += deposito
            print(f"Depósito de R${deposito} realizado com sucesso.")
        else:
            print("O valor do depósito deve ser maior que zero.")

    def sacar(self, saque): 
        if saque > 0:
            if self.saldo >= saque:
                self.saldo -= saque
                print(f"Saque de R${saque} realizado com sucesso.")
            else:
                print("Saldo insuficiente para realizar o saque.")
        else:
            print("O valor do saque deve ser maior que zero.")

    def consultar_saldo(self):
            print(f"Saldo atual da conta de {self.titular_conta}: R${self.saldo}")
                        #self.num_conta / #self.titular_conta
conta1 = ContaBancaria(int(input("Número de conta: ")),input("Nome do titular: "))
conta1.consultar_saldo() 

conta1.depositar(float(input("Valor a depositar: \n")))
conta1.consultar_saldo()  

conta1.sacar(float(input("Valor a sacar: \n"))) 
conta1.consultar_saldo()  