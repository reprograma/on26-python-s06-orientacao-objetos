# exercício 1

class ContaBancaria:
    def __init__(self, numero_conta, titular_conta):
        self.numero_conta = numero_conta
        self.titular_conta = titular_conta
        self.saldo = 0.0

    def depositar(self, valor):
        if valor > 0:
            self.saldo =+ valor
            print(f"Valor depositado de R${valor}, realizado com sucesso.")
        else:
            print("O valor do depósito deve ser maior que 0")
    
    def sacar(self, valor):
        if valor > 0:
            if self.saldo >= valor:
                self.saldo -= valor
                print(f"Saque de R${valor} realizado com sucesso.")
            else:
                print("Saldo insuficiente para realizar o saque.")
        else:
            print("O valor do saque dever ser maior que 0.")

conta = ContaBancaria(202301, "Daviny Letícia")

conta.depositar(100)

conta.sacar(10)

print(conta.saldo)


#Exercicio 2

class retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def calcular_area(self):
        return self.largura * self.altura

    def calcular_perimetro(self):
        return 2 * (self.largura + self.altura)

casa_fabiana = retangulo(5.0, 3.0)

print(f'A casa da Fabiana tem: {casa_fabiana.calcular_area()} área')
print(f'A casa da Fabiana tem: {casa_fabiana.calcular_perimetro()} de perímetro')

casa_daviny = retangulo(9.0, 10.5)

print(casa_daviny.calcular_area())
print(casa_daviny.calcular_perimetro())
print(casa_daviny.largura)

