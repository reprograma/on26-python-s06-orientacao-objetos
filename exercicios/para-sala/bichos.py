class Animal:
    def __init__(self, nome):
        self.nome=nome
    def fazer_som(self):
        pass

class cachorro(Animal):
    def fazer_som(self):
        return f'{self.fazer_som} late'
class gato(Animal):
    def fazer_som(self):
        return f'{self.fazer_som} mia muito'

cachorro_Mirley= cachorro('Frida')
cachorro_Mirley.fazer_som()
print(cachorro_Mirley.fazer_som)