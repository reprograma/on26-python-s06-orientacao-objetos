"""Exercício 1 - semama 06 (Conta Bancária)"""


class conta_bancaria:
    def __init__(self, numero_conta, nome_titular):
        self.numero_conta = numero_conta
        self.nome_titular = nome_titular
        self.saldo_conta = 0.0

    def depositar(self, deposito):
        if deposito > 0:
            self.saldo =+ deposito # =+ incrementador
            print(f'Valor depositado de R${deposito}, realizado com sucesso!')
        else:
            print("O valor do deposito de ser maior que R$0!")

    
    def sacar(self, saque):
            if saque > 0:
                if self.saldo >= saque:
                     self.saldo -= saque
                     print(f'Saque de R${saque}, realizado com sucesso!')
                else:
                 print("Saldo insuficiente para saque!")
            else: 
                print("O valor de saque deve ser maior que R$0!")

   
conta_dani = conta_bancaria(202301, "Dani Negrão")  

conta_dani.depositar(100)

conta_dani.depositar(50)

conta_dani.depositar(80)

conta_dani.sacar(10)
conta_dani.sacar(70)
conta_dani.depositar(1000)

print(f"Saldo em conta:R${conta_dani.saldo}")
   
