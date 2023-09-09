class Funcionario:
    def __init__(self, nome):
        self.nome = nome
        self.salario = 0

    def calcular_pagamento(self):
        pass #utilizado pois cada tipo de funcionário ira calcular da sua maneira pois existe 2 tipos. 

class FuncionarioTemporario(Funcionario):
    def __init__(self,nome,salario_por_hora,horas_trabalhadas):
        super().__init__(nome)
        self.salario_por_hora = salario_por_hora
        self.horas_trabalhadas = horas_trabalhadas

    def calcular_pagamento(self):
        pagamento = self.salario_por_hora * self.horas_trabalhadas
        return pagamento
    
class FuncionarioIntegral(Funcionario):
    def __init__(self, nome, salario_mensal):
        super().__init__(nome)
        self.salario_mensal = salario_mensal
        
    def calcular_pagamento(self):
        pagamento = self.salario_mensal
        return pagamento

funcionario_temporario = FuncionarioTemporario("Luana", 20.0, 40)

funcionario_integral = FuncionarioIntegral("Thaysa", 5000.0)

pagamento_temporario = funcionario_temporario.calcular_pagamento()
print(f"O pagamento para {funcionario_temporario.nome} é: R$ {pagamento_temporario:.2f}")

pagamento_integral = funcionario_integral.calcular_pagamento()

print(f"O pagamento para {funcionario_integral.nome} é: R${pagamento_integral:.2f}")
