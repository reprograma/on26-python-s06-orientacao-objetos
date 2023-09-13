class Vehicle:
    def __init__(self, model, year, price):
        self.model=model
        self.year=year
        self.price=price
    
    def calculate_tax(self):
        return 0.1*self.price
    
class Car(Vehicle):
    def __init__(self, model, year, price, mark):
        super().__init__(model, year, price)
        self.mark=mark

    def calculte_discount(self):
        return 0.05*self.price

class Motocycle(Vehicle):
    def __init__(self, model, year, price, cylinder_capacity):
        super().__init__(model, year, price)
        self.cylinder_capacity = cylinder_capacity
    
    def calculate_discount(self):
        return 0.05*self.price


suv= Car("Evoque", 2023, 427.950, "land Rover")
tax = suv.calculate_tax()
print(f'The tax amount is RS{tax}.')     
discount = suv.calculte_discount()
print(f'The discount amount is RS{discount}.')

naked = Motocycle("CB 500 f", 2023, 51.100, 500)
tax = naked.calculate_tax()
print(f'The tax amount is RS{tax}')
discount = naked.calculate_discount()
print(f'The discount amount is RS{discount}')
