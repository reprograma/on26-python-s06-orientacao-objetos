class Immobile:
    def __init__(self, address, proprietary_name, value_base):
        self.address = address
        self.proprietary_name = proprietary_name
        self.value_base = value_base
        
    def calculate_rental(self):
        return self.value_base
    
class House(Immobile):
    def __init__(self, address, proprietary_name, value_base, area_ground):
        super().__init__(address, proprietary_name, value_base)
        self.area_ground = area_ground
    
    def calculate_rental(self):
        resume = self.value_base + (self.area_ground * 5)
        return resume
    
        
class Apartment(Immobile):
    def __init__(self, address, proprietary_name, value_base, rooms):
        super().__init__(address, proprietary_name, value_base)
        self.rooms = rooms
    
    def calculate_rental(self):
        resume = self.value_base + (self.rooms * 300)
        return resume
    
house_Beyoncé = House("444, Street of glamurously", "Beyoncé", 1500, 300)
apartment_Bruna = Apartment("44, Street of Persistent", "Bruna Bodecam", 1200, 2)

print("Value of rental R$: ", house_Beyoncé.calculate_rental())
print("Value of rental R$: ", apartment_Bruna.calculate_rental())
    

    