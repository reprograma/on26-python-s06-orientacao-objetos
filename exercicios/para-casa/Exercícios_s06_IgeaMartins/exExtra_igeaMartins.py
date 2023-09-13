class funcionario:
    def __init__(self, nome):
        self.nome = str(nome)
        self.salario = 0
    
    def calculaPagamento(self):
        pass

class temporario(funcionario):
    def __init__(self, nome, salarioxhora, horas):
        super().__init__(nome)
        self.salarioxhora = float(salarioxhora)
        self.horas = float(horas)

    def calculaPagamento(self):
        salario = self.salarioxhora * self.horas
        return salario

class integral(funcionario):
    def __init__(self, nome, salarioxmes):
        super().__init__(nome)
        self.salarioxmes = int(salarioxmes)

    def desconto(self):
        salario = self.salarioxmes
        return salario


f46528 = temporario('Joana', 6500, 150)
print(f46528.calculaPagamento()) 

f46529 = integral('Darla', 20000.00)
print(f46529.desconto())

    