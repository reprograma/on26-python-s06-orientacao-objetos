
class ContaBancaria:

    def __init__ (self, num_conta,nome_titular): # saldo não pq é  zerado
        self.num_conta = num_conta
        self.nome_titular = nome_titular
        self.saldo_conta = 0.0
    
    def depositar(self, valor):
        if valor > 0: # tratamento d erro
            self.saldo_conta =+ valor
            print ( f' o valor depositado  é: ', valor)
        else:
            print( " o valor do deposito deve ser maior que 0.0")    
            #print( self.num_conta, self.saldo_conta)
            #self.valor = float(input('digite o valor a ser depositado' ))
            #print ( f' o saldo atual é: ', saldo_conta)
        
       
        
    
    def sacar( self, valor):
        if valor > 0:
            if self.saldo_conta >= 0:
                self.saldo_conta -= valor
                print(f'Saque de R$ {valor} realizado com sucesso')
            else:
            
                print("saldo insuficiente para realizar o saque")
        else:
             print("O valor do saque deve ser maior que zero.")  
            

ContaCarol = ContaBancaria( 202301, 'carol ribeiro')
ContaCarol.depositar(100)

ContaCarol.sacar(10)
print(ContaCarol.saldo_conta)

ContaLais = ContaBancaria( 202302, 'Lais')
ContaLais.depositar(80)
ContaLais.sacar(1000)
print(ContaLais.saldo_conta)