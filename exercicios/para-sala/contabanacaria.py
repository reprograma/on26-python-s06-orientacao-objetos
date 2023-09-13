class ContaBancaria:
    def __init__(self, Mirley, numero_conta):
        self.titulo=Mirley
        self.numero_conta= numero_conta
        self.saldo=0.0


    def depositar(self, valor):
        if valor>0:
            mensagem=f'Valor de depósito RS {valor} reias'
            self.saldo=+ valor
            print(mensagem)
        else:
            print("Depósito iválido")

    def sacar(self, valor):
        if valor >0:
            if self.saldo>=valor:
                self.saldo-=valor
                print(f'Saque no valor de RS{valor} realizada com sucesso')
            else:
                print("Saldo insuficiente")
        else:
            print("O saque deve ser maior que 0")

contaMirley = ContaBancaria(2301, "Mirley Mesquita")

contaMirley.depositar(1000)

contaMirley.sacar(20)

print(contaMirley.saldo)

contaDelise = ContaBancaria(2302, "Delise")

contaDelise.depositar(200)

contaDelise.sacar(1000)