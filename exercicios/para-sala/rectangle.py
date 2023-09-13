# Largura
# Altura

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def calculate_area(self):
        #print(f"Calculate area{self.width * self.height}")
        return self.width * self.height
        
    def calculate_perimeter(self):
        return 2 * (self.width + self.height)
    
house_Beyoncé = Rectangle(5.0, 3.0)
print(f"House of Beyoncé, have:\n {house_Beyoncé.calculate_area()} Area")
print(f"House of Beyoncé have {house_Beyoncé.calculate_perimeter()} Of Perimeter")

house_Bruna = Rectangle(9.0, 10.5)
print(house_Bruna.calculate_area())
print(house_Bruna.calculate_perimeter())


#     rectangle = rectangle(5.0, 3.0)
#     area = rectangle.calculate_area()
#     perimeter = rectangle.calculate_perimeter()

# print(f"Area of Rectangle:\n {area}")
# print(f"Perimeter of Rectangle:\n{perimeter}")