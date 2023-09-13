# Titular = holder
# Saldo = balance
# Numero da conta = account_number

class AccountBank():
    def __init__(self, account_number, holder):
        self.account_number = account_number
        self.holder = holder
        self.balance = 0.0
 
    def deposit(self, value):
        if value > 0:
            self.balance =+ value
            print(f"Deposit value R${value}, Successesfully done.")
        else:
            print("the deposit amount must be greater than 0 ")

    def withdraw(self, value):
        if value > 0:
            if self.balance >= value:
                self.balance -= value
                print(f"Withdraw R${value}, Successesfully done")
            else:
                print("Insufficient balance to withdraw.")
        else:
            print("The withdrawal amount must be greater than zero")
    
contaDaviny = AccountBank(202301, "Daviny Letícia")

contaDaviny.deposit(100)

contaDaviny.withdraw(10)

print(contaDaviny.balance)

contaLais = AccountBank(202302, "Lais")

contaLais.deposit(80)

contaLais.withdraw(1000)
    # def account_number(self):
    # print(f"Account number:\n")
    
