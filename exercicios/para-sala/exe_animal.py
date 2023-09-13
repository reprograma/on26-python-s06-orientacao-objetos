

class Animal:
    def __init__(self, nome):
        self.nome = nome
        
    def fazer_som(self):
        pass
    
class Cachorro(Animal):
    def fazer_som(self):
       return f"{self.nome} faz um latido"
   
    def andar(self):
       pass
   

class Gato(Animal):
    def fazer_som(self):
        return f"{self.nome} faz um miado"


mel = Gato ("mel")

mel.fazer_som()

print(mel)