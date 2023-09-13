class Vehicle:
    def __init__(self, hallmark, model, age, especification, value_base):
        self.hallmark = hallmark
        self.model = model
        self.age = age
        self.especification = especification
        self.value_base = value_base
        
    def calculate_taxes(self):
        self.value_base = round(self.value_base * 1.1)
        return self.value_base
    
class Car(Vehicle):
    def __init__(self, hallmark, model, age, especification, value_base):
        super().__init__(hallmark, model, age, especification, value_base)
        self.value_base = value_base
    
    def calculate_discount(self):
        resume = round(self.value_base * 0.95)
        return resume
    
        
class Motorcycle(Vehicle):
    def __init__(self, hallmark, model, age, especification, value_base):
            super().__init__(hallmark, model, age, especification, value_base)
            self.value_base = value_base
    
    def calculate_taxes_m(self):
        self.value_base = round(self.value_base * 1.05)
        return self.value_base
    
car = Car(f"BMW", "i7 Sedan", 2024, "4 Doors Eletric", 1282950)
print(" BMW Model i7 Sedan 2024 4 Doors Eletric\n",
      "Value Base", car.calculate_taxes(),"\n" 
      " Value to pay", car.calculate_discount(),"\n\n")

motorcycle = Motorcycle(f"BMW", "1250 GS", 2024, "Cylinder 1254", 95990 )
print(" BMW Model 1250 GS 2024 Cylinder 1.254\n", 
      "Value Base", motorcycle.calculate_taxes(),"\n"
      " Value to pay", motorcycle.calculate_taxes_m())