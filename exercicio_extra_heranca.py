#exercicio extra
class Funcionarios:
    def __init__(self, nome):
        self.nome = nome
        self.salario_base = 0.0
        
    def calcular_pagamento():
        return self.salario_base
        pass
class FuncionarioTemporario (Funcionarios):
    def __init__(self, nome,  salario_por_hora, horas_trabalhadas):
        super().__init__(nome)
        self.salario_por_hora = salario_por_hora
        self.horas_trabalhadas = horas_trabalhadas
    def calcular_pagamento(self):
        pagamento = self.salario_por_hora * self.horas_trabalhadas
        return pagamento
class FuncionarioIntegral (Funcionarios):
    def __init__(self,nome, salario_mensal):
        super().__init__(nome)
        self.salario_mensal = salario_mensal
    def calcular_pagamento(self):
        return self.salario_mensal
func_temporario = FuncionarioTemporario ('Amanda',5.0, 360)
func_integral = FuncionarioIntegral ('Marcela', 450.00)
 
print(f" Salário do Funcionário Temporário: {func_temporario.calcular_pagamento()}")

print(f" Salário do Funcionário Integral:{func_integral.calcular_pagamento()}")


    