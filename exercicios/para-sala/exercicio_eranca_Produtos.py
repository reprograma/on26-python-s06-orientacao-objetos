class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
        
        
    def descricao ( self):
        return f'Nome: {self.nome}, Preco: {self.preco}' 
    
class ProdutoFisico( Produto):
    def __init__(self, nome,preco,peso, dimencoes):
                 
                 # 
        super().__init__ (nome,preco)  
        self.peso = peso
        self.dimencoes = dimencoes
    def descricao(self):  
       return super().descricao() + f'Peso: {self.peso}, Dimenções: { self.dimencoes}'    



class  ProdutoDigital(Produto):
    def __init__(self, nome,preco,tamanho_arq, tipo):
                 
                 # 
        super().__init__ (nome,preco)  
        self.tamanho_arq = tamanho_arq
        self.tipo= tipo
    def descricao(self):  
       return super().descricao() + f'Tamanho_arq: {self.tamanho_arq}, Tipo: { self.tipo}'    
   
   
   
produto_fisico = ProdutoFisico ('mesa', 100.00, 20, '2x2x1.5')    
print (produto_fisico.descricao())
produto_digital = ProdutoDigital('manual antirracista', 100.00, 12, 'E-book')
print (produto_digital.descricao())