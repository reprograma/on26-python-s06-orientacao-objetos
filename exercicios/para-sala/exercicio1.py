# exercicio 1

class conta_bancaria:
    def __init__ (self, numero_conta, titular_conta):
        self.numero_conta = numero_conta
        self.titular_conta = titular_conta
        self.saldo = 0.0
    
    def depositar(self, valor):
        if valor > 0:
            self.saldo =+ valor    #ou também pode ser self.saldo = self.saldo + valor
            print(f'Valor depositado de R${valor}, realizado com sucesso.')
        else:
            print('O valor do depósito deve ser maior que 0.')
    
    def sacar(self, valor):
        if valor > 0:
            if self.saldo >= valor:
                self.saldo -= valor
                print(f'Saque de R${valor} realizado com sucesso')
            else:
                print('Saldo insuficiente')
        else:
            print('O valor a ser sacado deve ser maior que 0.')

contaMari = conta_bancaria(202301, "Marimari")
contaMari.depositar(100)
contaMari.sacar(50)
print(contaMari.saldo)

contaLais = conta_bancaria(202302, "Lais")
contaLais.depositar(500)
contaLais.sacar(1000)
print(contaLais.saldo)
    

    

    

